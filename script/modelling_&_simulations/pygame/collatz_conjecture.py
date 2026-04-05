# code by patrick derry (2026)
import pygame
from pygame.locals import *
from sys import exit

# https://en.wikipedia.org/wiki/Collatz_conjecture

# the conjecture function uses n as input
# (first if-clause in while-loop)
# other calculations render (turn, n)
# in terms of (x, y) in pygame window

# initialization
# get starting number from user
# transform into x,y coordinates in pygame window
n = int(input("Starting number? (Recommend 100) "))
x = 5
y = 465 - 15*n
nextN = n
ready = True
turn = 0
show=0
savedPoints = list()

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # each calculated value is rendered as a circle 
    # draw white circle       
    pygame.draw.circle(screen, (255,255,255), (x,y), 5)
    
    if ready:
        n = nextN
        if n % 2:
            nextN = 3*n + 1
        else:
            nextN = n/2
        savedPoints.append((x,y))
        turn+=1
        ready=False
        
    if not x == 5 + 15*turn:
        x += 1
    if not y == 465 - 15*nextN:
        if y > 465 - 15*nextN:
            y -= abs(nextN - n)
        else:
            y += abs(nextN - n)

    if (x == 5 + 15*turn) and y == 465 - 15*nextN:
        ready=True
        
    for circle in savedPoints:
        # draw red circles
        pygame.draw.circle(screen, (255,0,0), circle, 5)
        
    pygame.display.update()
