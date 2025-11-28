import pygame as pg
#crear una plantilla enemiga
class Turret(pg.sprite.Sprite)  :
  def __init__(self, pos, image) -> None:
    pg.sprite.Sprite.__init__(self) #Image aspector 
    self.image= image
    self.rect = self.image.get_rect()
    self.rect.center = pos 
