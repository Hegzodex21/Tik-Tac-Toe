import NTSFunc
try:
    import pygame
except:
    import os
    os.system("pip install pygame")
    import pygame
from system import *


pygame.init()

Arial = pygame.font.SysFont("Arial", 30)
class Rectangle:
    def __init__(self, rectStats):
        self.rect = pygame.Rect(rectStats)
        self.color = (0,0,0)
        self.clickedOne = False
        self.turn = 0
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

        mousePos = pygame.mouse.get_pos()
        mouseButton = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mousePos):
            self.color = (128,128,128)
        else:
            self.color = (0,0,0)

        if self.rect.collidepoint(mousePos) and mouseButton[0] and self.clickedOne == False:
            self.clickedOne = True
            self.turn = turn
            global used
            used = True
        
        if self.clickedOne:
            shape = pygame.image.load(NTSFunc.folderInName + "/Images/" + self.turn + ".png").convert_alpha()
            surface.blit(shape, self.rect)



screen = pygame.display.set_mode((602,602))
rect1 = Rectangle((0,0,200,200))
rect2 = Rectangle((201,0,200,200))
rect3 = Rectangle((402,0,200,200))
rect4 = Rectangle((0,201,200,200))
rect5 = Rectangle((201,201,200,200))
rect6 = Rectangle((402,201,200,200))
rect7 = Rectangle((0,402,200,200))
rect8 = Rectangle((201,402,200,200))
rect9 = Rectangle((402,402,200,200))

# Vars
global x
global turn
turn = 0
x = 0
used = False
winner = 0
resetButton = Image("Reset")
changeScreen = False

run = True
while run or run == None:
    if changeScreen == True:
        screen = pygame.display.set_mode((602,602))
        changeScreen = False
    screen.fill((255,255,255))
    rect1.draw(screen)
    rect2.draw(screen)
    rect3.draw(screen)
    rect4.draw(screen)
    rect5.draw(screen)
    rect6.draw(screen)
    rect7.draw(screen)
    rect8.draw(screen)
    rect9.draw(screen)

    if x == 0:
        turn = "cross"
    if x == 1:
        turn = "circle"

    if x == 0 and used == True:
        x = 1
        used = False
    elif x == 1 and used == True:
        x = 0
        used = False
    if True:
        if rect1.turn == "cross" and rect5.turn == "cross" and rect9.turn == "cross":
            winner = "cross"
        elif rect7.turn == "cross" and rect5.turn == "cross" and rect3.turn == "cross":
            winner = "cross"
        elif rect1.turn == "cross" and rect4.turn == "cross" and rect7.turn == "cross":
            winner = "cross"
        elif rect2.turn == "cross" and rect5.turn == "cross" and rect8.turn == "cross":
            winner = "cross"
        elif rect3.turn == "cross" and rect6.turn == "cross" and rect9.turn == "cross":
            winner = "cross"
        elif rect1.turn == "cross" and rect2.turn == "cross" and rect3.turn == "cross":
            winner = "cross"
        elif rect4.turn == "cross" and rect5.turn == "cross" and rect6.turn == "cross":
            winner = "cross"
        elif rect7.turn == "cross" and rect8.turn == "cross" and rect9.turn == "cross":
            winner = "cross"
        if rect1.turn == "circle" and rect2.turn == "circle" and rect3.turn == "circle":
            winner = "circle"
        elif rect1.turn == "circle" and rect5.turn == "circle" and rect9.turn == "circle":
            winner = "circle"
        elif rect7.turn == "circle" and rect5.turn == "circle" and rect3.turn == "circle":
            winner = "circle"
        elif rect1.turn == "circle" and rect4.turn == "circle" and rect7.turn == "circle":
            winner = "circle"
        elif rect2.turn == "circle" and rect5.turn == "circle" and rect8.turn == "circle":
            winner = "circle"
        elif rect3.turn == "circle" and rect6.turn == "circle" and rect9.turn == "circle":
            winner = "circle"
        elif rect1.turn == "circle" and rect2.turn == "circle" and rect3.turn == "circle":
            winner = "circle"
        elif rect4.turn == "circle" and rect5.turn == "circle" and rect6.turn == "circle":
            winner = "circle"
        elif rect7.turn == "circle" and rect8.turn == "circle" and rect9.turn == "circle":
            winner = "circle"
        elif rect1.turn != 0 and rect2.turn != 0 and rect3.turn != 0 and rect4.turn != 0 and rect5.turn != 0 and rect6.turn != 0 and rect7.turn != 0 and rect8.turn != 0 and rect9.turn != 0:
            winner = "Nobody"
    
    if winner != 0:
        runWinner = True
        changeScreen = True
        while runWinner:
            
            screen.fill((255,255,255))
            screen.blit(Arial.render(f"{winner} is the winner!", True, (0,0,0)), (180,275))

            if changeScreen == True:
                screen = pygame.display.set_mode((602,702))
                changeScreen = False

            resetButton.draw(screen, 250, 610)

            if resetButton.rect.collidepoint(vars()[0]) and vars()[1][0]:
                rect1.clickedOne = False
                rect2.clickedOne = False
                rect3.clickedOne = False
                rect4.clickedOne = False
                rect5.clickedOne = False
                rect6.clickedOne = False
                rect7.clickedOne = False
                rect8.clickedOne = False
                rect9.clickedOne = False
                rect1.turn = 0
                rect2.turn = 0
                rect3.turn = 0
                rect4.turn = 0
                rect5.turn = 0
                rect6.turn = 0
                rect7.turn = 0
                rect8.turn = 0
                rect9.turn = 0
                runWinner = False
                changeScreen = True
                winner = 0

            quitGame()

            pygame.display.update()


    quitGame()
    pygame.display.update()