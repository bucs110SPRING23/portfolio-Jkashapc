import pygame
pygame.init()
screen=pygame.display.set_mode()
screen.fill("green")
pygame.display.flip()
pygame.draw.circle(screen, "red", [200,150],25)
pygame.draw.circle(screen, "red",[200,200], 40)
pygame.draw.circle(screen, "red",[200,260],60)
pygame.display.flip()
pygame.time.wait(2000)
