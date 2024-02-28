import pygame as pg
from random import randrange

WIDTH = 1200
HEIGHT = 800

fps = 60

paddle_width = 330
paddle_height = 35
paddle_speed = 15
paddle = pg.Rect(WIDTH // 2 - paddle_width, HEIGHT - paddle_height - 10, paddle_width, paddle_height)

ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pg.Rect(randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

block_list = [pg.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(randrange(30, 256), randrange(30, 256), randrange(30, 256)) for i in range(10) for j in range(4)]

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Breakout")
clock = pg.time.Clock()

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y < delta_x:
        dx = -dy
    return dx, dy

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill("black")

    [pg.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]

    pg.draw.rect(screen, "darkorange", paddle)
    pg.draw.circle(screen, "white", ball.center, ball_radius)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius:
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hit_index = ball.collidelist(block_list)

    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)

    key = pg.key.get_pressed()
    if key[pg.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pg.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pg.display.flip()
    clock.tick(fps)