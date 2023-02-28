from EasyPyGame import *

PyGame = EasyPyGame()
PyGame.CreateWindow(960, 540, True, "EasyPyGame Test")

PyGame.CreateObject('Player.png')

while PyGame.IsRunning:
    PyGame.FillScreen((200, 200, 200))
    
    for Object in PyGame.Objects:
        Object.Rect = Object.Image.get_rect(topleft=(Object.X, Object.Y))
        PyGame.DrawToScreen(Object.Image, Object.Rect)
    
    PyGame.Update()
