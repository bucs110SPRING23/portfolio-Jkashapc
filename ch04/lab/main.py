import random 
import pygame
import math
screen=pygame.display.set_mode()
ss=pygame.display.get_window_size()
print(ss)
screen.fill('black')
pygame.display.flip()
user_guess=[]
done = False
pygame.draw.rect(screen, 'blue', [0,902.5,601.5,601.5])
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            screen.fill('black')
            pygame.draw.circle(screen,'green',(ss[0]/2,ss[1]/2),ss[1]/2)
            pygame.draw.line(screen,'orange',(0,ss[1]/2),(ss[0],ss[1]/2),5)
            pygame.draw.line(screen,'orange',(ss[0]/2,0),(ss[0]/2,ss[1]),5)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.display.flip()
            for i in range (10):
                x1=random.randrange(0,ss[0])
                y1=random.randrange(0,ss[1])
                dist_from_center=math.hypot(x1-ss[0]/2,y1-ss[1]/2)
                in_circ = (dist_from_center <= ss[1]/2)
                if in_circ:
                    pygame.draw.circle(screen, 'green', (x1,y1),5)
                else:
                    pygame.draw.circle(screen, 'orange', (x1,y1),5)
                pygame.display.flip()
                pygame.time.wait(1000)  
            
  
            pygame.time.wait(2000)
            pygame.display.flip()
