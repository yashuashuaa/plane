import pygame

class Buttle(pygame.sprite.Sprite):

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("E:\plane\images\\bullet1.png")
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=20
        self.active=False
        self.mask=pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top-=self.speed
        if self.rect.top<0:
            self.active=False

    def reset(self,position):
        self.active=True
        self.rect.left,self.rect.top=position

class Buttle2(pygame.sprite.Sprite):

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("E:\plane\images\\bullet2.png")
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=40
        self.active=False
        self.mask=pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top-=self.speed
        if self.rect.top<0:
            self.active=False

    def reset(self,position):
        self.active=True
        self.rect.left,self.rect.top=position
