import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import sys
def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    elif (event.type == pygame.QUIT):
      sys.exit()


def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,56)
  pygame.draw.rect(screen, (255,255,255),
                   (60,580,840,80), 1)
  if len(message) != 0:
    
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                (80,600))
    pygame.display.update()
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question  + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question  + string.join(current_string,""))
  return string.join(current_string,"")

def type_box():
  screen = pygame.display.set_mode((960,720)) 
  print ask(screen, "") + " was entered"

def main():
  pygame.init()
  background_colour = (0,0,0)
  pygame.display.set_caption('Typo Rihno')
  screen = pygame.display.set_mode((960,720)) 
  screen.fill(background_colour) 
  while True:     
    type_box()

main()