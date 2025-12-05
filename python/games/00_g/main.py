try:
 import pygame as pg 
 from enemy import Enemies
 from character import Character
 import os
 from turret import Turret
 import config as cg
except ImportError as e :
    print("error al importar la libreri---<> ",e)

# craar la plantilla del juego RootGame
class RootGame:
  def __init__(self):
      self.pg = pg.init()
      self.screen = pg.display.set_mode((cg.screen_width,cg.screen_height))
      self.clock = pg.time.Clock()
      self.cwd = os.getcwd()
      self.load_assets()
      self.create_goup()
      self.draw_weadpoint()
      self.instance()

  def load_assets(self):
      self.player1_image = pg.image.load(os.path.join(self.cwd,"pr","games","00_g","asset","enemies","enemy1.png")).convert_alpha()
      self.enemy_image = pg.image.load(os.path.join(self.cwd,"pr","games","00_g","asset","enemies","enemy1.png")).convert_alpha()
      self.turret_image = pg.image.load(os.path.join(self.cwd,"pr","games","00_g","asset","turret","turret1.png")).convert_alpha()

  def create_goup(self):
     self.enemi_group = pg.sprite.Group()
     self.player_group = pg.sprite.Group()
     self.turret_group = pg.sprite.Group()
 
  def draw_weadpoint(self):
    self.weadpoints = [
      (300,300),
      (100,300),
      (100,600),
      (300,700),
      (400,500),
      (500,200),
      (500,300),
      (700,400),
      (500,500),
      (100,400)
    ]
     
  def instance(self):
    enemy1 =Enemies (self.weadpoints[0] ,self.enemy_image)
    self.enemi_group.add(enemy1)
    self.player1 = Character((300,300),self.player1_image)


  def run(self):
      run = True
      delta = 0
      speed = 100
      
      while run:
        self.screen.fill("gray100") #color de fondo de la ventana
        pg.draw.lines(self.screen,"blue",True,self.weadpoints)
        self.enemi_group.update(speed*delta)
        self.enemi_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.turret_group.draw(self.screen)

        keys = pg.key.get_pressed() #guardar la tecla precionada
        # mover a la derecha
        if keys[pg.K_d] or keys[pg.K_RIGHT]: 
          self.player1.move_right(speed*delta)
        elif keys[pg.K_a] or keys[pg.K_LEFT]:
          self.player1.move_left(speed*delta)
        elif keys[pg.K_w]or keys[pg.K_UP]: 
          self.player1.move_up(speed*delta)
        elif keys[pg.K_s]or keys[pg.K_DOWN]:
          self.player1.move_down(speed*delta)
        
        for event in pg.event.get():
          if event.type == pg.QUIT:
               run = False

          if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
               print("mouse click", event.pos)
        
        delta = self.clock.tick(cg.fps) /1000
         

        # inicializar la ventana
        pg.display.flip()
        #limitar los fps a 60 frames segundo
        self.clock.tick(cg.fps) 

      pg.quit()
root = RootGame()
root.run()