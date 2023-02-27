import pygame 
import random 
import math
screen=pygame.display.set_mode()
screen.fill('black')
pygame.display.flip()
pygame.draw.circle(screen,'red',(900,600),600)
pygame.draw.line(screen,'blue',(0,600),(2000,600),5)
pygame.draw.line(screen,'blue',(900,0),(900,2000),5)
pygame.display.flip()
pygame.time.wait(3000)
pygame.display.flip()
dist_from_center=math.hypot(random.randrange(0,2000), random.randrange(0,2000))
in_circ= dist_from_center <= 5/2
for i in range (10):
    pygame.draw.circle(screen, 'green', (dist_from_center),5)
    pygame.display.flip()
    break
pyga,e.time.wait(1000)
pygame.display.flip()
