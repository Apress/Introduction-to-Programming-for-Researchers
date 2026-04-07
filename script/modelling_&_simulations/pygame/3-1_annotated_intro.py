#!/usr/bin/env python 
# code by harrison kinsley and will mcgugan
# comments by james derry
# Beginning Python Games Development With Pygame, 2dEd., Apress (2015), pp 43-47
# available for digital download

# these files are within the same dir as the script
# if you get: pygame.error: File is not a Windows BMP file
# comment out these lines and uncomment their bmp equivalents beneath
background_image_filename = 'sushiplate.jpg'  
mouse_image_filename = 'fugu.png' 
#background_image_filename = 'sushiplate.bmp'  
#mouse_image_filename = 'fugu.bmp'
 
import pygame 
from pygame.locals import * 
from sys import exit  

#### begin initialization ####
pygame.init() 
 
screen = pygame.display.set_mode((640, 480), 0, 32) 
pygame.display.set_caption("Hello, World!") 
 
background = pygame.image.load(background_image_filename).convert() 
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha() 
#### end initialization ####

# infinite loop
# while program is running, it is doing so by executing the code
# entirely within this loop.
while True: 
    # process event in event queue
    for event in pygame.event.get(): 
        # the only event we're interested in
        # in this bare-bones scripts
        if event.type == QUIT:
            pygame.quit()
            exit() 
        # blitting means copying from one image to another
        # these changes are held in a buffer in memory
        # until we invoke display.update()
        screen.blit(background, (0,0))
        
        # update cursor position within game window
        x, y = pygame.mouse.get_pos() 
        x-= mouse_cursor.get_width() / 2 
        y-= mouse_cursor.get_height() / 2
        # this blit captures the change in mouse position
        screen.blit(mouse_cursor, (x, y)) 
        # all the changes in the pygame image are held in a buffer.
        # we invoke them to update the entire display at one time
        # with the display.update() method at the end of the for-loop
        pygame.display.update()
