#!/usr/bin/python
import pygame
import sys
from pygame.locals import *
#from gi.repository import Gtk

file = open("lewa.txt")
article =  str(file.readlines())
file.close()


class TestGame:
    # runs when class instantiates
    def __init__(self):
	# instance variable defaults
        self.background = pygame.image.load("background.png")
        self.rihno = pygame.image.load("rihno.png")
        self.poacher = pygame.image.load("poacher.png")
        self.rx = 240
        self.ry = 0
        self.px = 10
        self.py = 0
        self.List = article.split(" ") 
        self.count = 0
        self.current_word = ''
        self.CurrentQuestion = ''
    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass
    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass
    # The main game loop.
    def word_display(self):
        pass
    #def wordlist()
    def run(self):
        print self.List
        self.running = True 
        direction_right = True
	# get the surface to draw on
        screen = pygame.display.get_surface()
        while True:
        #while self.running:
            # Pump GTK messages.
            #while Gtk.events_pending():
                #Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.count += 1


            # Clear Display
            screen.fill((0, 0, 0))  # 255 for white
            self.current_word = self.List[self.count]
            
            font = pygame.font.Font("african.ttf",30)
            Current_word = font.render(self.current_word,False,(250,250,250))
            screen.blit(Current_word,(200,640))
            
            screen.blit(self.background, (0, 0))
            font = pygame.font.Font("african.ttf",30)

            

            CurrentWord1 = font.render("Current",False,(250,250,250))
            CurrentWord2 = font.render("Word:",False,(250,250,250))
            screen.blit(CurrentWord1,(20,640))
            screen.blit(CurrentWord2,(20,670))
            YourWord1 = font.render("Your",False,(250,250,250))
            YourWord2 = font.render("Word:",False,(250,250,250))
            screen.blit(YourWord1,(500,640))
            screen.blit(YourWord2,(500,670))
            pygame.draw.rect(screen,(255,255,255),(460,620,10,120))
            # Draw the ball
            screen.blit(self.rihno,(self.rx, self.ry))
            screen.blit(self.poacher,(self.px, self.py))

            if (direction_right == True):
                self.px += 10
                if (self.px >= 900):
                    self.poacher = pygame.transform.flip(self.poacher,1,0) 
                    direction_right = not direction_right
                    self.py += 80
            elif (direction_right == False):
                self.px -= 10
                if (self.px <= 0):
                    self.poacher = pygame.transform.flip(self.poacher,1,0) 
                    direction_right = not direction_right
                    self.py += 80
            
            elif (self.px == 80 and self.py >= 600):
                sys.exit()

            
            # Flip Display
            pygame.display.flip()


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_caption('Typo Rihno')
    pygame.init()
    screen = pygame.display.set_mode((960,720))   
    game = TestGame()
    game.run()
    game.word_display()
   


if __name__ == '__main__':
    main()
