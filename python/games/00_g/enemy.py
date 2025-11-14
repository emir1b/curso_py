import pygame as pg 
#crear una plantilla enemiga 
class Enemies(pg.sprite.Sprite) :
    def __init__(self,pos,image):#method
        pg.sprite.Sprite.__init__(self) #heredar las imagenes de py game
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.move()

    def move(self):
       self.rect.x += 1 


      
    
    


