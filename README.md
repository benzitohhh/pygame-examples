# Pygame examples


## To install pygame (should work on OSX and python3)

```pip install pygame```


## Source code and examples

To find path to sourcecode, run this in the python repl:
```
import pygame
print(pygame.__file__)
```

Examples are in th `examples` subdirectory.


## Running examples in emacs

Open an example file (i.e. `/examples/aliens.py`

Modify any `__file__` imports to `'__file__'` (as emacs does not know about that variable.

Do `C-c C-p` (run-python)

Do `C-c C-c` (python-shell-send-buffer)

Then either call `main()` directly in the console.

More coneniently, add a `main()` call to the sourcecode. Then each `C-c C-c` will reload and run the game.

Doing keyboard interrupt in the console (`C-c C-c`) will stop the pygame engine. But note the window will remain on the screen.

Killing the python console (`C-x k ret`) will close the pygame window.
