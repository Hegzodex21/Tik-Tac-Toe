import pygame
import NTSFunc


# Class

class Image:
    def __init__(self, imageFileName, scale=1):
        imageFileName = NTSFunc.folderInName + "/Images/" + imageFileName + ".png"
        self.image = pygame.image.load(imageFileName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pressed = False
        
    def draw(self, surface, x=0, y=0):
        self.rect.topleft = (x,y)
        surface.blit(self.image, (self.rect.x, self.rect.y))



# Functions

def vars():
    mousePos = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()
    keyPressed = pygame.key.get_pressed()
    return mousePos, mousePressed, keyPressed

def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            NTSFunc.clear()