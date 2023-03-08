# EasyPyGame
EasyPyGame is a python library built upon pygame that aims to make game development easier
<br/>
## Features
•Easy setup
<br/>
•Helps simplify code
<br/>
•Has built-in functions for rotating objects
<br/>
•Makes rendering text easy
<br/>
<br/>

## How to add EasyPyGame to your project
1. Download EasyPyGame.py and insert it into the directory of your module
2. Put "from EasyPyGame import *" at the top of the module
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
e.g. EasyPyGame.CreateWindow(1920, 1080, True, "Best Game Ever")
<br/>
<br/>

#### .SetWindowIcon(path)
_.SetWindowIcon()_ sets the icon of the EasyPyGame window
<br/>
"path" is the path to the icon image
<br/>
e.g. EasyPyGame.SetWindowIcon("/Assets/WindowIcon.png")
<br/>
<br/>

#### .Update()
_.Update()_ updates the game. This checks if the game has been closed and renders any changes made
<br/>
e.g. EasyPyGame.Update()
<br/>
<br/>

#### .FillScreen(color)
_.FillScreen()_ fills the screen with a color
<br/>
"color" is the color the screen is to be filled with. Input the R, G, and B values into parenthesis
<br/>
e.g. EasyPyGame.FillScreen((200, 200, 200))
<br/>
<br/>

#### .FPS()
_.FPS()_ returns the current frames per second of the game
<br/>
e.g. print(EasyPyGame.FPS())
<br/>
<br/>

#### .CreateObject(path)
_.CreateObject()_ creates a game object with a image
<br/>
"path" is the path to the image of the object
<br/>
e.g. EasyPyGame.CreateObject('Player.png')
<br/>
You can set a easy to remember name by doing something like:
<br/>
Player = EasyPyGame.Objects[0]
<br/>
<br/>

#### .CreateText(text, font, fontsize, aa, color)
_.CreateText()_ creates text that can be drawn to the screen.
<br/>
"text" is the text you want to display (String)
<br/>
"font" is the path to the ttf font you want to use
<br/>
"fontsize" is the size of text (Integer)
<br/>
"aa" is whether or not the text will use anti-aliasing (Boolean)
<br/>
"color" is the color of the text. Input the R, G, and B values into parenthesis
<br/>
e.g. EasyPyGame.CreateText("Hello!", 'Arial.ttf', 50, True, (255, 255, 255))
<br/>
<br/>

#### .DrawToScreen(object, rect)
_.DrawToScreen()_ draws a object to the screen
<br/>
"object" is the image attribute of a object that is to be drawn
<br/>
"rect" is the x and y position of the object inside of parenthesis
<br/>
e.g. EasyPyGame.DrawToScreen(Player.Image, Player.Rect)
<br/>
<br/>

#### .KeyPressed(key)
_.KeyPressed()_ returns "True" or "False" if the set key is pressed or not
<br/>
"key" is the key to be checked for a press (String)
<br/>
e.g. if EasyPyGame.KeyPressed("Up"):
<br/>
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
_.PlayMusic()_ plays a file as music
<br/>
"path" is the path to the music file (String)
<br/>
"fade" is the time in milliseconds that the music fades in (Integer)
<br/>
e.g. EasyPyGame.PlayMusic('epicsong.ogg', 500)
<br/>
<br/>

#### .CreateSound(path)
_.CreateSound()_ returns a sound that can be played
<br/>
"path" is the path to the sound file
<br/>
e.g. Sound = EasyPyGame.CreateSound('sound.wav')
<br/>
<br/>

#### .PlaySound(sound)
_.PlaySound()_ plays the input sound
<br/>
e.g. EasyPyGame.PlaySound(Sound)
<br/>
<br/>

#### .StopMusic()
_.StopMusic()_ stops and unloads the currently playing song
<br/>
e.g. EasyPyGame.StopMusic()
<br/>
<br/>

#### .StopSounds()
_.StopSounds()_ stops all sound effects playing (this excludes the currently playing music)
<br/>
e.g. EasyPyGame.StopSounds
<br/>
<br/>

#### .Collision(rect1, rect2)
_.Collision()_ checks for a collision between 2 object rects
<br/>
"rect1" and "rect2" are the rects that will be checked for collision
<br/>
e.g. if EasyPyGame.Collision(Player.Rect, Enemy.Rect):
<br/>
<br/>

#### .RotationToPosition(x1, y1, x2, y2)
_.RotationToPosition()_ calculates the rotation angle from (x1, y1) to (x2, y2)
<br/>
"x1" and "y1" are the first pair of coordinates (Integers)
<br/>
"x2" and "y2" are the second pair of coordinates (Integers)
<br/>
e.g. PlayerAngle = EasyPyGame.RotationToPosition(Player.X, Player.Y, Mouse.X, Mouse.Y)
<br/>
<br/>

#### .RotateImage(image, angle)
_.RotateImage()_ rotates the provided image to the given angle
<br/>
"image" is the .Image attribute of a object
<br/>
"angle" is the angle the image will be rotated (Integer)
<br/>
e.g. EasyPyGame.RotateImage(Player.Image, PlayerAngle)
<br/>
<br/>

#### .StopAudio()
_.StopAudio()_ stops all currently playing audio
<br/>
e.g. EasyPyGame.StopAudio()
<br/>
<br/>

### Variables
"IsRunning" is the variable that checks if the game is supposed to be running (Boolean)
<br/>
"Objects" is a list of all game objects (List)
<br/>
"ObjectCount" keeps count of the amount of game objects (Integer)
<br/>
"DeltaTime" is the time since the last frame was rendered (Integer)
<br/>
"X" and "Y" are exclusive to objects, and they determine the position of a object (Integer)
