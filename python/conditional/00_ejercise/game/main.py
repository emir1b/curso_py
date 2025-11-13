# Example file showing a circle moving on screen
import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
run = True
dt = 0
speed = 500


# Posición del jugador 
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while run:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pg.draw.circle(screen, "red", player_pos, 40)

    keys = pg.key.get_pressed() # Guardar la tecla precionada
    if keys[pg.K_w] or keys[pg.K_UP]:
        player_pos.y -= speed * dt
    if keys[pg.K_s]  or keys[pg.K_DOWN]:
        player_pos.y += speed * dt
    if keys[pg.K_a]  or keys[pg.K_LEFT]:
        player_pos.x -= speed * dt
    if keys[pg.K_d]  or keys[pg.K_RIGHT]:
        player_pos.x += speed * dt

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit() 
