import pygame 
def threenp1(n):
    cnt=0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
        cnt+=1
    return cnt
def threenp1range(upper_limit):
    objinseq={}
    for i in range(2,upper_limit+1):
        var=threenp1(i)
        objinseq[i]=var
    return objinseq
def gcoord(threen1plus1):
    coord = list(threen1plus1.items())
    print(coord)
    window = pygame. display. set_mode (size=(640, 480))
    window.fill("black")
    pygame. draw. lines (window, "white", True, points=coord)
    new_display = pygame.transform. flip(window, False, True)
    window.blit (new_display, (0, 0))
    width, height = new_display.get_size()
    factor = 2
    print((width * factor, height * factor))
    new_display = pygame.transform.scale(new_display, (width * factor, height * factor))
    window.blit(new_display, (width * factor, height * factor))
    pygame.display.flip()
def main():
    dict=threenp1range
    print(dict)
    gcoord(dict)

pygame.init()

while 1:
   pygame.event.pump()
   main()
   pygame.time.wait(3000)
   break




