import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('E:\plane\images\enemy1.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)
        self.speed=2
        self.active=True
        self.destory_image=[]
        self.destory_image.extend([pygame.image.load("E:\plane\images\enemy1_down1.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy1_down2.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy1_down3.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy1_down4.png").convert_alpha()])
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)
        self.active = True

class MidEnemy(pygame.sprite.Sprite):
    energy=8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('E:\plane\images\enemy2.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-10*self.height,-self.height)
        self.speed=1
        self.active = True
        self.destory_image = []
        self.destory_image.extend([pygame.image.load("E:\plane\images\enemy2_down1.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy2_down2.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy2_down3.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy2_down4.png").convert_alpha()])
        self.mask = pygame.mask.from_surface(self.image)
        self.energy=MidEnemy.energy
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-10*self.height,-self.height)
        self.active = True
        self.energy=8
class BigEnemy(pygame.sprite.Sprite):
    energy=20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.image.load('E:\plane\images\luo.png').convert_alpha()

        self.image=pygame.image.load('E:\plane\images\enemy3_n1.png').convert_alpha()
        self.image2=pygame.image.load('E:\plane\images\enemy3_n2.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-15*self.height,-5*self.height)
        self.speed=1
        self.active = True
        self.destory_image = []
        self.destory_image.extend([pygame.image.load("E:\plane\images\enemy3_down1.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy3_down2.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy3_down3.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy3_down4.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy3_down5.png").convert_alpha(), \
                                   pygame.image.load("E:\plane\images\enemy3_down6.png").convert_alpha()])
        self.mask=pygame.mask.from_surface(self.image)
        self.energy=BigEnemy.energy
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-10*self.height,-self.height)
        self.active = True
        self.energy=20
