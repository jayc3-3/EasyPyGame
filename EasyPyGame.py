print("Made with EasyPyGame 1.0.1")
import pygame
import math

class Object():
    X = 0
    Y = 0
    
    def __init__(self, path):
        self.Image = pygame.image.load(path)
        self.Image.convert()
        self.Rect = self.Image.get_rect(topleft=(self.X, self.Y))

class EasyPyGame():
    IsRunning = True
    Objects = []
    Clock = pygame.time.Clock()
    DeltaTime = Clock.tick(60) / 1000
    ObjectCount = 0
    
    def __init__(self):
        pygame.init()
    
    def CreateWindow(self, width, height, resizable, title):
        if resizable == True:
            self.Window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        else:
            self.Window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.Screen = self.Window.copy()
    
    def SetWindowIcon(self, path):
        pygame.display.set_icon(pygame.image.load(str(path)))

    def FPS(self):
        fps = round(self.Clock.get_fps())
        return fps
    
    def FillScreen(self, color):
        self.Screen.fill(color)
    
    def DrawToScreen(self, obj, rect):
        self.Screen.blit(obj, rect)
    
    def CreateObject(self, path):
        self.ObjectCount += 1
        self.Objects.append(Object(path))
        print("EasyPyGame: Created object #" + str(self.ObjectCount))
        return(self.Objects[(self.ObjectCount - 1)])
    
    def CreateText(self, text, font, fontsize, aa, color):
        Font = pygame.font.Font(font, fontsize)
        Text = Font.render(text, aa, color)
        return Text
    
    def RotationToPosition(self, x1, y1, x2, y2):
        relx, rely = (x2 - x1), (y2 - y1)
        angle = int(math.degrees(math.atan2(-rely, relx)))
        return angle
    
    def RotateImage(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        return rotated
    
    def Collision(self, rect1, rect2):
        if rect1.colliderect(rect2):
            return True
        
        return None
    
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
    
    def PlayMusic(self, path, fade):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0.0, fade)
    
    def StopMusic(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    
    def CreateSound(self, path):
        Sound = pygame.mixer.Sound(path)
        return Sound
    
    def StopSounds(self):
        pygame.mixer.stop()
    
    def PlaySound(self, sound):
        sound.play()

    def StopAudio():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.stop()

    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.IsRunning = False
        
        if self.IsRunning:
            self.DeltaTime = self.Clock.tick(60) / 1000
            
            for Obj in self.Objects:
                Obj.Rect = Obj.Image.get_rect(topleft=(Obj.X, Obj.Y))
        
            self.Window.blit(pygame.transform.scale(self.Screen, self.Window.get_rect().size), (0, 0))
            pygame.display.flip()
