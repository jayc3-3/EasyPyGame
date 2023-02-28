# EasyPyGame
A library that makes creating games with PyGame simple as possible

## How to add EasyPyGame to your project
1. Download EasyPyGame.py and insert it into the directory of your module
<br/>
2. Put from EasyPyGame import * near the top of the module
<br/>
3. Create a instance of EasyPyGame by using PyGame = EasyPyGame(). "PyGame" can be switched out with any undefined variable
<br/>
<br/>

## Documentation
### .CreateWindow(width, height, resizable, title)
_.CreateWindow()_ creates a pygame window.
<br/>
"width" sets the width of the window (Int)
<br/>
"height" sets the height of the window (Int)
<br/>
"resizable" defines if the window should be resizable or not (Boolean)
<br/>
"title" defines the title of the created window (String)
<br/>
<br/>

### .Update()
_.Update()_ updates the game. This checks if the game has been closed and renders any changes made
<br/>
<br/>

### .KeyPressed(key)
_.KeyPressed()_ returns a "True" or "False" if the set key is pressed.
<br/>
"key" is the key to be checked for a press (String)
<br/>
<br/>

#### All valid keys
"Up" = Up arrow key
<br/>
"Down" = Down arrow key
<br/>
"Left" = Left arrow key
<br/>
"Right" = Right arrow key
<br/>
"W" = W key
<br/>
"S" = S key
<br/>
"A" = A key
<br/>
"D" = D key
<br/>
"Enter" = Enter key
