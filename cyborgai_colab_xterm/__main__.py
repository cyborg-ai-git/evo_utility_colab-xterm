import cyborgai_colab_xterm
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='python -m cyborgai_colab_xterm')
    parser.add_argument("-p", "--port", type=int,
                        help="port number", default=10000)
    parser.add_argument("command", help="Commands to run", nargs=argparse.REMAINDER)
    args, unknown = parser.parse_known_args()
    # Combine parsed command args with any unknown args
    command = args.command + unknown
    port = args.port

    term = cyborgai_colab_xterm.XTerm(command, port)
    term.open()
