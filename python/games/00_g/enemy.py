import pygame as pg
#crear una plantilla enemiga
class Enemies (pg.sprite.Sprite)  :
  def __init__(self,pos,image) -> None:
    pg.sprite.Sprite.__init__(self) #Image aspector 
    self.image= image
    self.rect = self.image.get_rect()
    self.rect.center = pos 

  def upgrade(self,new_pos=None):
    self.move(new_pos)
  
  def move(self,new_pos=None):
    self.rect.x += new_pos
    

