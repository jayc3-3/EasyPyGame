from EasyPyGame import *

PyGame = EasyPyGame()
PyGame.CreateWindow(960, 540, True, "EasyPyGame Test")

PyGame.CreateObject('Player.png')

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

    for Object in PyGame.Objects:
        Object.Rect = Object.Image.get_rect(topleft=(Object.X, Object.Y))
        PyGame.DrawToScreen(Object.Image, Object.Rect)
    
    PyGame.DrawToScreen(ShowcaseText, (100, 100))
    PyGame.DrawToScreen(FPSText, (25, 25))
    
    PyGame.Update()