> Thanks:
> 

# cyborgai-colab-xterm
CyborgAI Colab-xterm allows you to open a terminal in a cell with command injection support.


1. Install package and load the extension
    ```
    !pip install cyborgai-colab-xterm
    %load_ext cyborgai_colab_xterm
    ```ad_ext colabxterm
    ```
2. Open a terminal
    ```
    %xterm
    ```
3. Enjoy!

Try it out in the demo notebook. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/infuseai/colab-xterm/blob/main/demo.ipynb)

# Features
- TTY support
- Does not block your kernel

# Options

```
%xterm height=1000 port=10001 command="ls -l"
```

option | description
-------|-----------
height | The height of the terminal panel
port | The server port
command | Command to execute when terminal opens (NEW FEATURE!)

# Screenshots
![](assets/colab-xterm.png)



