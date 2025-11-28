import pygame as pg
class Character(pg.sprite.Sprite): # Heredar sprite de pygame
  def __init__(self,pos, imagen): #metodo constructor
    pg.sprite.Sprite.__init__(self) #Image aspector 
    self.image = imagen
    self.rect = self.image.get_rect()
    self.rect.center = pos

  #metodo para mover a la derecha
  def move_right(self,new_pos): # recibir la nueva posicion(new_pos)
    #actualizar posicion
    self.rect.x += new_pos
    
  #metodo para mover a la derecha
  def move_left(self,new_pos): # recibir la nueva posicion(new_pos)
    #actualizar posicion
    self.rect.x -= new_pos
  #metodo para mover a la derecha
  def move_up(self,new_pos): # recibir la nueva posicion(new_pos)
    #actualizar posicion
    self.rect.y -= new_pos
  #metodo para mover a la derecha
  def move_down(self,new_pos): # recibir la nueva posicion(new_pos)
    #actualizar posicion
    self.rect.y += new_pos
