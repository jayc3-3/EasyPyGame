import pygame

class Object():
    X = 0
    Y = 0
    
    def __init__(self, pathtoimage):
        self.Image = pygame.image.load(pathtoimage)
        self.Image.convert()
        self.Rect = self.Image.get_rect(topleft=(self.X, self.Y))

class EasyPyGame():
    IsRunning = True
    Objects = []
    ObjectAmount = 0
    Clock = pygame.time.Clock()
    DeltaTime = Clock.tick(60) / 1000
    
    def __init__(self):
        pygame.init()
    
    def CreateWindow(self, width, height, flags):
        self.Window = pygame.display.set_mode((width, height), flags)
        self.Screen = self.Window.copy()
    
    def FPS(self):
        fps = round(self.Clock.get_fps())
        return fps
    
    def FillScreen(self, color):
        self.Screen.fill(color)
    
    def DrawToScreen(self, image, rect):
        self.Screen.blit(image, rect)
    
    def CreateObject(self, pathtoimage):
        self.Objects.append(Object(pathtoimage))
        self.ObjectAmount += 1
    
    def KeyPressed(self, key):
        if key == "Up":
            if pygame.key.get_pressed()[pygame.K_UP]:
                return True

        elif key == "Down":
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                return True

        elif key == "Left":
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                return True

        elif key == "Right":
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                return True
        
        elif key == "W":
            if pygame.key.get_pressed()[pygame.K_w]:
                return True

        elif key == "A":
            if pygame.key.get_pressed()[pygame.K_a]:
                return True

        elif key == "S":
            if pygame.key.get_pressed()[pygame.K_s]:
                return True

        elif key == "D":
            if pygame.key.get_pressed()[pygame.K_d]:
                return True

        elif key == "Enter":
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                return True
        
        return None
    
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.IsRunning = False
        
        if self.IsRunning:
            self.DeltaTime = self.Clock.tick(60) / 1000
        
            self.Window.blit(pygame.transform.scale(self.Screen, self.Window.get_rect().size), (0, 0))
            pygame.display.flip()
