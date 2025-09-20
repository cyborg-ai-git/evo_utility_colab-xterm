import asyncio
from typing import List
import tornado.ioloop
import tornado.web
import base64
from ptyprocess import PtyProcess
import os
from . import manager


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('client/dist/index.html')


class StdoutHandler(tornado.web.RequestHandler):
    def initialize(self, process, initial_command=None):
        self.process = process
        self.initial_command = initial_command
        self.command_sent = False

    async def get(self):
        loop = asyncio.get_event_loop()
        try:
            # Send initial command on first read if we have one
            if self.initial_command and not self.command_sent:
                print(f"DEBUG: Sending initial command on first stdout read: '{self.initial_command}'")
                command_with_newline = self.initial_command + '\n'
                self.process.write(command_with_newline.encode())
                self.command_sent = True
                
            b = await loop.run_in_executor(None, lambda:  self.process.read(4*1024*1024))
            self.write(b)
            await self.flush()
        except EOFError as e:
            pass


class StdinHandler(tornado.web.RequestHandler):
    def initialize(self, process):
        self.process = process

    async def get(self, base64str):
        data = base64.b64decode(base64str)
        self.process.write(data)


class ResizeHandler(tornado.web.RequestHandler):
    def initialize(self, process):
        self.process = process

    async def get(self):
        rows = int(self.get_argument('rows'))
        cols = int(self.get_argument('cols'))
        self.process.setwinsize(rows, cols)


class XTerm:
    def __init__(self, argv: List, port=10000):
        self.argv = argv
        self.port = port
        self.initial_command = None
        
        print(f"DEBUG: XTerm.__init__ received argv: {argv}")
        
        # If we have a command, store it to send after shell starts
        if argv and len(argv) > 0:
            self.initial_command = ' '.join(argv)
            print(f"DEBUG: Initial command set to: '{self.initial_command}'")

    def open(self):
        port = self.port
        # Always start with a normal shell
        argv = [os.getenv("SHELL", '/bin/sh')]

        try:
            process = PtyProcess.spawn(argv)
            
            print(f"DEBUG: Setting up tornado app with initial_command: {self.initial_command}")
            
            staticFolder = os.path.join(
                os.path.dirname(__file__), "client/dist")
        except Exception as e:
            manager.write_info_file(os.getpid(), False, str(e))

        try:
            app = tornado.web.Application([
                (r"/out", StdoutHandler, dict(process=process, initial_command=self.initial_command)),
                (r"/in/(.*)", StdinHandler, dict(process=process)),
                (r"/resize", ResizeHandler, dict(process=process)),
                (r"/(.*\.js)", tornado.web.StaticFileHandler,
                 {"path": staticFolder}),
                (r'/', MainHandler),
            ])
            app.listen(port, "127.0.0.1")
            print(f"🚀  Listen to {port}")
            manager.write_info_file(os.getpid(), True)
        except Exception as e:
            manager.write_info_file(os.getpid(), False, str(e))
            raise e

        tornado.ioloop.IOLoop.current().start()
