import pygame
from pygame.locals import *
from Piano import Piano

# Initialize pygame and set up display, color variables, buttons and button text
pygame.init()
white = (255,255,255)
black = (0,0,0)
display_width = 640
display_heigth = 400
menuDisplay = pygame.display.set_mode((display_width, display_heigth))
startButton = pygame.Rect(270,175,100,50)
startFont = pygame.font.SysFont(None, 48)
startText = startFont.render('Start', True, white, black)
startTextRect = startText.get_rect()
startTextRect.centerx = startButton.centerx
startTextRect.centery = startButton.centery
def menu():
  menu = True
  while menu:
    for event in pygame.event.get():
      # print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        print(mouse_pos)
        if startButton.collidepoint(mouse_pos):
          # print("HI!")
          myPiano = Piano()
          myPiano.play()
          quit()
      menuDisplay.fill(white)
      pygame.draw.rect(menuDisplay, black, startButton)
      menuDisplay.blit(startText, startTextRect)
      pygame.display.update()
menu()