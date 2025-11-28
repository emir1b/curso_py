import pygame as pg
from enemy import Enemies
from character import Character
import os
from turret import Turret

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

#cargar imagenes 
player_image= pg.image.load(os.path.join(cwd, "pr/games/00_g/asset/enemies/enemy1.png"))
enemy_image= pg.image.load(os.path.join(cwd, "pr/games/00_g/asset/enemies/enemy1.png"))

#punto de recorido del enemigo
weadpoints = [
  (300,300),
  (100,300),
  (100,600),
  (100,700),
  (400,100),
  (500,200),
  (600,300),
  (700,400),
  (800,500),
  (200,700)
]
#crear grupo de enemigos
enemy_group = pg.sprite.Group()
#crear enemigos
enemy1 =Enemies (weadpoints[0] ,enemy_image)

#agregar enemigos al grupo enemies
enemy_group.add(enemy1)
turret_group = pg.sprite.Group()
player_group = pg.sprite.Group()
#crear grupo player

#crear players
player1 =Character ((100,100),player_image)
#agregar players al grupo enemies
player_group.add(player1)
delta=0
speed=300
while run :

  screen.fill("gray") #color de fondo de la ventana
  pg.draw.lines(screen,"blue",True,weadpoints)
  enemy_group.update(speed*delta)
  enemy_group.draw(screen)
  player_group.draw(screen)
  turret_group.draw(screen)
  #renderizar el juego aqui

  keys = pg.key.get_pressed() #guardar la tecla precionada
  # mover a la derecha
  if keys[pg.K_d]: 
    player1.move_right(speed*delta)
  elif keys[pg.K_a]:
    player1.move_left(speed*delta)
  elif keys[pg.K_w]: 
    player1.move_up(speed*delta)
  elif keys[pg.K_s]:
    player1.move_down(speed*delta)

  delta = clock.tick(60) /1000

  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
    
  # inicializar la ventana
  pg.display.flip()
  #limitar los fps a 60 frames segundo
  clock.tick(60) 

pg.quit()