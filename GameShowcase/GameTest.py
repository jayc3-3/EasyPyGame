#This is a example of a game made with EasyPyGame that utilizes the features of the library
from EasyPyGame import *

PyGame = EasyPyGame()
PyGame.CreateWindow(960, 540, True, "EasyPyGame Game")

PyGame.CreateObject('Player.png')

Player = PyGame.Objects[0]

while PyGame.IsRunning:
    PyGame.FillScreen((200, 200, 200))
    
    ShowcaseText = PyGame.CreateText("Made with EasyPyGame!", 'Arial.ttf', 50, True, (0, 0, 0))
    
    FPSText = PyGame.CreateText("FPS: " + str(PyGame.FPS()), 'Arial.ttf', 25, True, (0, 0, 0))
    
    if PyGame.KeyPressed('Up'):
        PyGame.Objects[0].Y -= int(325 * PyGame.DeltaTime)

    if PyGame.KeyPressed('Down'):
        PyGame.Objects[0].Y += int(325 * PyGame.DeltaTime)

    if PyGame.KeyPressed('Left'):
        PyGame.Objects[0].X -= int(325 * PyGame.DeltaTime)

    if PyGame.KeyPressed('Right'):
        PyGame.Objects[0].X += int(325 * PyGame.DeltaTime)
    
    if Player.X < -20:
        Player.X = 980
    elif Player.X > 980:
        Player.X = -20
    
    if Player.Y < -20:
        Player.Y = 560
    elif Player.Y > 560:
        Player.Y = -20

    for Object in PyGame.Objects:
        PyGame.DrawToScreen(Object.Image, Object.Rect)
    
    PyGame.DrawToScreen(ShowcaseText, (100, 100))
    PyGame.DrawToScreen(FPSText, (25, 25))
    
    PyGame.Update()
