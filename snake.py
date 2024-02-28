import pygame as pg
import random

WINDOW_SIZE = 400

TILE_SIZE = 10

apple_pos = random.randrange(0, WINDOW_SIZE, TILE_SIZE), random.randrange(0, WINDOW_SIZE, TILE_SIZE)

x = random.randrange(0, WINDOW_SIZE, TILE_SIZE)
y = random.randrange(0, WINDOW_SIZE, TILE_SIZE)

snake = [(x, y)]
snake_length = 1

deltaX = 0
deltaY = 0

fps = 15

pg.init()
screen = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if not deltaX == 1:
                    deltaX = -1
                    deltaY = 0
            elif event.key == pg.K_RIGHT:
                if not deltaX == -1:
                    deltaX = 1
                    deltaY = 0
            elif event.key == pg.K_UP:
                if not deltaY == 1:
                    deltaX = 0
                    deltaY = -1
            elif event.key == pg.K_DOWN:
                if not deltaY == -1:
                    deltaX = 0
                    deltaY = 1

    x += deltaX * TILE_SIZE
    y += deltaY * TILE_SIZE

    snake.append((x, y))
    snake = snake[-snake_length:]

    if snake[-1] == apple_pos:
        apple_pos = random.randrange(0, WINDOW_SIZE, TILE_SIZE), random.randrange(0, WINDOW_SIZE, TILE_SIZE)
        snake_length += 1
    if (x < 0) or (y < 0) or (x > WINDOW_SIZE - TILE_SIZE) or (y > WINDOW_SIZE - TILE_SIZE):
        break

    screen.fill("black")

    for i, j in snake:
        pg.draw.rect(screen, "green", (i, j, TILE_SIZE, TILE_SIZE))

    pg.draw.rect(screen, "red", (apple_pos[0], apple_pos[1], TILE_SIZE, TILE_SIZE))

    pg.display.flip()
    clock.tick(fps)
