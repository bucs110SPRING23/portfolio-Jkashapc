import pygame 
def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None
def threenp1range(upper_limit):
    objinseq={}
    for i in range(2,upper_limit):
        var=threenp1(i)
        objinseq[i]=var
    return objinseq
def gcoord(threen1plus1):
   pygame.init()
   scrn=pygame.dislpay.set_mode()
   scrn.fill('black')
   factor = 2
   new_display = pygame. transform. flip(window, False, True)
   width, height = new_display.get_size()
   new_display = pygame. transform.scale(new_display, (width * factor, height * factor))


