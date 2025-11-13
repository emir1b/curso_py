import pygame as pg 
#crear una plantilla enemiga 
class Persona :
       def __init__(self):#method


       

       class Empleado(Persona):#se hereda los atributos y metodoso de la clase Persona  
    def __init__(self,name,edad,salary):#method
       super().__init__(name,edad)
       self.salary = salary

empleado= Empleado("perri",90,55)
print(empleado.name)
print(empleado.edad)
print(empleado.salary)

import pygame as pg 
#crear una plantilla enemiga 
class Enemies(pg.Sprite.Sprite) :
    def __init__(self,pos,image):#method
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def upgrade(self):
        self.move()

    def move(self):
       self.rect.x += 1 