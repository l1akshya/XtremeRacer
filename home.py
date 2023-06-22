import pygame
import sys
import race
import math
import random
from race import main
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((1188,648))#setting up the screen size
pygame.display.set_caption("XTREME RACER")#game title
icon=pygame.image.load("carz.png")#game title
pygame.display.set_icon(icon)
home_screen=pygame.image.load("home_screen.png")#loading the background for start screen
start_playing=pygame.image.load("play.png").convert_alpha()#play button for start screen
background_music=mixer.music.load(r"C:\Users\LAKSHYA\Desktop\XtremeRacer\background_music.mp3")
mixer.music.play(-1)
image = pygame.image.load('play.png')

# Get the original image size
original_size = image.get_size()
scale_factor=2
# Calculate the new size after scaling
new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))

# Create a new surface with the new size
start_playing = pygame.transform.scale(image, new_size)
options_playing=pygame.image.load("options.png").convert_alpha()#options button for start screen
exit_playing=pygame.image.load("exit.png").convert_alpha()#exit button for start screen

#class for buttons
class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    def draw(self):
        action=False
        position_mouse=pygame.mouse.get_pos()
        if self.rect.collidepoint(position_mouse):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False :
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0 and self.clicked == True:
                self.clicked=False

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

start_button=button(520+128+128+30,162+256,start_playing)
options_button=button(520+256+30,290+180-5,options_playing)
exit_button=button(520+256+30,418+110-20,exit_playing)

running=True#program running
while running:
    screen.fill((0, 0, 0))#preset screen colour
    screen.blit(home_screen,(0,0))#setting up the background
    #setting the buttons
    if start_button.draw():
        print("Start")
        pygame.quit()
        main()

    #options_button.draw()
        
    if exit_button.draw():
        pygame.quit()
        print("Exit")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()