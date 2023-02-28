# EasyPyGame
A library that makes creating games with PyGame simple as possible

## How to add EasyPyGame to your project
1. Download EasyPyGame.py and insert it into the directory of your module
2. Put "from EasyPyGame import *" near the top of the module
3. Create a instance of EasyPyGame by using PyGame = EasyPyGame(). "PyGame" can be switched out with any undefined variable
<br/>
<br/>

## Documentation
### Functions
#### .CreateWindow(width, height, resizable, title)
_.CreateWindow()_ creates a pygame window.
<br/>
"width" sets the width of the window (Integer)
<br/>
"height" sets the height of the window (Integer)
<br/>
"resizable" defines if the window should be resizable or not (Boolean)
<br/>
"title" defines the title of the created window (String)
<br/>
<br/>

#### .Update()
_.Update()_ updates the game. This checks if the game has been closed and renders any changes made
<br/>
<br/>

#### .FillScreen(color)
_.FillScreen()_ fills the screen with a color
"color" is the color the screen is to be filled with. Input the R, G, and B values into parenthesis _i.e. .FillScreen((255, 255, 255))_
<br/>
<br/>

#### .FPS()
_.FPS()_ returns the current frames per second of the game
<br/>
<br/>

#### .CreateObject(pathtoimage)
_.CreateObject()_ creates a game object with a image
"pathtoimage" is the path to the image of the object _i.e. .CreateObject('Player.png')_
<br/>
<br/>

#### .CreateText(text, font, fontsize, aa, color)
_.CreateText()_ creates text that can be drawn to the screen.
"text" is the text you want to display (String)
"font" is the path to the ttf font you want to use _i.e. 'Arial.ttf'_
"fontsize" is the size of text (Integer)
"aa" is whether or not the text will use anti-aliasing (Boolean)
"color" is the color of the text. Input the R, G, and B values into parenthesis _i.e. .CreateText("Hello!", 'Arial.ttf', 50, True, (255, 255, 255))_
<br/>
<br/>

#### .DrawToScreen(object, rect)
_.DrawToScreen()_ draws a object to the screen
"object" is the object to be drawn
"rect" is the x and y position of the object inside of a parenthesis _i.e. (50, 100) or the .Rect if it's being used on a object created with .CreateObject()_
<br/>
<br/>

#### .KeyPressed(key)
_.KeyPressed()_ returns a "True" or "False" if the set key is pressed
<br/>
"key" is the key to be checked for a press (String)
<br/>

##### All valid keys
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
