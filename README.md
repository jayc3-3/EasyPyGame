# EasyPyGame
EasyPyGame is a library that aims to make game development easier

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
<br/>
"color" is the color the screen is to be filled with. Input the R, G, and B values into parenthesis _e.g. .FillScreen((255, 255, 255))_
<br/>
<br/>

#### .FPS()
_.FPS()_ returns the current frames per second of the game
<br/>
<br/>

#### .CreateObject(pathtoimage)
_.CreateObject()_ creates a game object with a image
<br/>
"pathtoimage" is the path to the image of the object _e.g. .CreateObject('Player.png')_
<br/>
_All objects created by this method are added to a list called '.Objects'. You can identify specific objects by assigning them a new name. e.g. 'Player = EasyPyGame.Objects[0]'_
<br/>
<br/>

#### .CreateText(text, font, fontsize, aa, color)
_.CreateText()_ creates text that can be drawn to the screen.
<br/>
"text" is the text you want to display (String)
<br/>
"font" is the path to the ttf font you want to use _e.g. 'Arial.ttf'_
<br/>
"fontsize" is the size of text (Integer)
<br/>
"aa" is whether or not the text will use anti-aliasing (Boolean)
<br/>
"color" is the color of the text. Input the R, G, and B values into parenthesis _e.g. .CreateText("Hello!", 'Arial.ttf', 50, True, (255, 255, 255))_
<br/>
<br/>

#### .DrawToScreen(object, rect)
_.DrawToScreen()_ draws a object to the screen
<br/>
"object" is the object to be drawn
<br/>
"rect" is the x and y position of the object inside of a parenthesis _e.g. (50, 100) or the .Rect if it's being used on a object created with .CreateObject()_
<br/>
<br/>

#### .KeyPressed(key)
_.KeyPressed()_ returns "True" or "False" if the set key is pressed or not
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
<br/>
<br/>

#### .PlayMusic(path, fade)
_.PlayMusic()_ plays a .mp3 or .ogg file as music
<br/>
"path" is the path to the music file (String)
<br/>
"fade" is the time in milliseconds that the music fades in (Integer)9
<br/>
<br/>

#### .CreateSound(path)
_.CreateSound()_ returns a sound that can be played
<br/>
"path" is the path to the sound file
<br/>
Call .play() on the sound to play the audio
<br/>
<br/>

### Variables
"IsRunning" is the variable that checks if the game is supposed to be running (Boolean)
<br/>
"Objects" is a list of all game objects (List)
<br/>
"DeltaTime" is the time since the last frame was rendered (Integer)
<br/>
"X" and "Y" are exclusive to objects, and they determine the position of a object (Integer)
