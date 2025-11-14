import pygame as pg 
class Character(pg.sprite.Sprite):


  def character(pg, screen, dt):
    #pocición del jugador
    player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    pg.draw.circle(screen, "red", player_pos, 40)

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_a]:
        player_pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_pos.x += 300 * dt
