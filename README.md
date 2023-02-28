# EasyPyGame
A library that makes creating games with PyGame simple as possible

## How to add EasyPyGame to your project
1. Download EasyPyGame.py and insert it into the directory of your module

2. Put "from EasyPyGame import *" near the top of the module

3. Create a instance of EasyPyGame by using PyGame = EasyPyGame(). "PyGame" can be switched out with any undefined variable

## Documentation
### .CreateWindow(width, height, resizable, title)
_.CreateWindow()_ creates a pygame window.

"width" sets the width of the window (Int)

"height" sets the height of the window (Int)

"resizable" defines if the window should be resizable or not (Bool)

"title" defines the title of the created window (String)

### .Update()
_.Update()_ updates the game. This checks if the game has been closed and renders any changes made

### .KeyPressed(key)
_.KeyPressed()_ returns a "True" or "False" if the set key is pressed.

"key" is the key to be checked for a press (String)

#### All valid keys
"Up" = Up arrow key

"Down" = Down arrow key

"Left" = Left arrow key

"Right" = Right arrow key

"W" = W key

"S" = S key

"A" = A key

"D" = D key

"Enter" = Enter key
