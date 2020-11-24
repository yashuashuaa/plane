#我操控的飞机
import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.destory_image=[]
        self.image=pygame.image.load('E:\plane\images\me1.png').convert_alpha()
        self.image2= pygame.image.load('E:\plane\images\me2.png').convert_alpha()
        self.destory_image.extend([pygame.image.load("E:\plane\images\me_destroy_1.png").convert_alpha(),\
                                   pygame.image.load("E:\plane\images\me_destroy_2.png").convert_alpha(),\
                                   pygame.image.load("E:\plane\images\me_destroy_3.png").convert_alpha()])
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,(self.height-self.rect.top)-60
        self.speed=10
        self.active = True
        self.wudi=False
        self.mask=pygame.mask.from_surface(self.image)
    def moveUp(self):
        if self.rect.top>0:
            self.rect.top-=self.speed
        else:
            self.rect.top=0

    def moveDown(self):
        if self.rect.bottom<self.height:
            self.rect.top+=self.speed
        else:
            self.rect.bottom=self.height

    def moveLeft(self):
        if self.rect.left>0:
            self.rect.left-=self.speed
        else:
            self.rect.left=0

    def moveRight(self):
        if self.rect.right<self.width:
            self.rect.left+=self.speed
        else:
            self.rect.right=self.width

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - 100)-60
        self.wudi=True
        #print(self.rect.left,self.rect.top)