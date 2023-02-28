#This is the same game made without EasyPyGame
import pygame

pygame.init()

Window = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
Screen = Window.copy()
pygame.display.set_caption("Without EasyPyGame")

class Object():
    X = 0
    Y = 0
    
    def __init__(self, pathtoimage):
        self.Image = pygame.image.load(pathtoimage)
        self.Image.convert()
        self.Rect = self.Image.get_rect(topleft=(self.X, self.Y))

Player = Object('Player.png')

Clock = pygame.time.Clock()

Font1 = pygame.font.Font('Arial.ttf', 50)
Font2 = pygame.font.Font('Arial.ttf', 25)

Running = True

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    DeltaTime = Clock.tick(60) / 1000
    
    FPS = round(Clock.get_fps())
    
    if pygame.key.get_pressed()[pygame.K_UP]:
        Player.Y -= int(325 * DeltaTime)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        Player.Y += int(325 * DeltaTime)

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        Player.X -= int(325 * DeltaTime)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        Player.X += int(325 * DeltaTime)

    if Player.X < -20:
        Player.X = 980
    elif Player.X > 980:
        Player.X = -20
    
    if Player.Y < -20:
        Player.Y = 560
    elif Player.Y > 560:
        Player.Y = -20

    Player.Rect = Player.Image.get_rect(topleft=(Player.X, Player.Y))
    
    Screen.fill((200, 200, 200))

    ShowcaseText = Font1.render("Made without EasyPyGame", True, (0, 0, 0))

    FPSText = Font2.render("FPS: " + str(FPS), True, (0, 0, 0))
    
    Screen.blit(Player.Image, Player.Rect)
    Screen.blit(ShowcaseText, (100, 100))
    Screen.blit(FPSText, (25, 25))
    
    Window.blit(pygame.transform.scale(Screen, Window.get_rect().size), (0, 0))
    pygame.display.flip()

pygame.quit()
