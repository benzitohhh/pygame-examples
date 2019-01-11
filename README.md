# Pygame examples


## To install pygame (should work on OSX and python3)

```pip install pygame```


## Docs

are here https://www.pygame.org/docs/py-modindex.html

## Source code and examples

The pygame sourcecode is on github here: https://github.com/pygame/pygame

To find path to sourcecode locally, run this in the python repl:
```
import pygame
print(pygame.__file__)
```

Sourcecode file `sprite.py` contains a lot of useful classes (i.e. `Sprite`, `Group` etc).

Example games are in the `/examples` subdirectory.



## Running examples in emacs

Open an example file (i.e. `/examples/aliens.py`)

Modify any `__file__` imports to `'__file__'` (as emacs does not know about that variable.

Add a `main()` call to the sourcecode.

Do `C-c C-p` (run-python) - starts a python shell.

Do `C-c C-c` (python-shell-send-buffer) - sends the code to the python shell.

To reload game:

a) Stop the game (either by quitting it on the window, or doing a keyboard interrupt in the console). Note that the window stays.

b) `C-c C-c` - to restart the game

Killing the python console (`C-x k ret`) will close the pygame window.
