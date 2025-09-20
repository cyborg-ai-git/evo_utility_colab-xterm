<img src="https://avatars.githubusercontent.com/u/129898917?v=4" alt="cyborgai" width="256" height="256">

---

## [CyborgAI](https://github.com/cyborg-ai-git) (https://github.com/cyborg-ai-git)

---

# cyborgai_peer

---

> ⚠️ **BETA DISCLAIMER**: CyborgAI_peer is currently in beta version. Use at your own risk. Features may be unstable and subject to change without notice. This software is provided "as is" without warranty of any kind.

---

## License
Apache License Version 2.0, January 2004
# cyborgai-colab-xterm
CyborgAI Colab-xterm allows you to open a terminal in a cell with command injection support.


### Install
1. Install package and load the extension
    ```
    !pip install git+https://github.com/cyborg-ai-git/evo_utility_colab-xterm.git
    %load_ext cyborgai_colab_xterm
    ```
2. Open a terminal
    ```
    %xterm
    ```
---

> **Try CyborgAI_peer:**
> 
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/cyborg-ai-git/evo_utility_colab-xterm/blob/main/colab/demo.ipynb)


---

# Features
- TTY support
- Does not block your kernel
- Command exec

---

# Options

```
%xterm height=1000 port=10001 command="ls -l"
```

option | description
-------|-----------
height | The height of the terminal panel
port | The server port
command | the command to execute 

---

> ### Thanks:
> https://colab.research.google.com/github/infuseai/colab-xterm

---