import random 
import pygame
import math
pygame.init()
screen=pygame.display.set_mode()
ss=pygame.display.get_window_size()
print(ss)
screen.fill('black')
pygame.display.flip()
user_guess=[]
done = False
pygame.display.flip()
height=600
width=600
numplay=2
play=0
score=[0,0]
color1=['red','blue']
color2=['orange','yellow']
pygame.draw.rect(screen,'red',(0,902.5,902.5,1203))
pygame.display.flip()
pygame.draw.rect(screen, 'blue',(905.2,1805,1805,1203))
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            screen.fill('black')
            pygame.draw.circle(screen,'grey',(ss[0]/2,ss[1]/2),ss[1]/2)
            pygame.draw.line(screen,'orange',(0,ss[1]/2),(ss[0],ss[1]/2),5)
            pygame.draw.line(screen,'orange',(ss[0]/2,0),(ss[0]/2,ss[1]),5)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.display.flip()
            for i in range (10*numplay):
                x1=random.randrange(0,ss[0])
                y1=random.randrange(0,ss[1])
                dist_from_center=math.hypot(x1-ss[0]/2,y1-ss[1]/2)
                in_circ = (dist_from_center <= ss[1]/2)
                if in_circ:
                    pygame.draw.circle(screen,color1[play], (x1,y1),10)
                    score[play]+=1
                else:
                    pygame.draw.circle(screen,color2[play], (x1,y1),10)
                pygame.display.flip()
                pygame.time.wait(1000)
                play=(play+1)%2
                print(score)
            f=pygame.font.Font(None,50)
            if score[0]>score[1]:
                text=f.render("Player 1 won",True,"purple")
                screen.blit(text,(0,0))
            elif score[0]<score[1]:
                text=f.render("Player 2 won",True,"purple")
                screen.blit(text,(0,0))

            
            
  
            pygame.time.wait(2000)
            pygame.display.flip()
