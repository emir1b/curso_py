try:
 import pygame as pg 
 from enemy import Enemies
 from character import Character
 import os
 from turret import Turret
except ImportError as e :
    print("error al importar la libreri---<> ",e)

# craar la plantilla del juego RootGame
class RootGame:
   def __init__(self)
      self.pg = pg.init()
      self.screem
#distanciar la clase RootGame



cwd = os.getcwd()
print(cwd)
#crear la ventana del juego 
pg.init() #inicializar la ventana
#tamaño de la ventana 
screen = pg.display.set_mode((800,720))
 #tasa de frame 60
clock = pg.time.Clock()
run = True
dt = 0