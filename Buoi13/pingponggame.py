import pygame

pygame.init()
pygame.display.set_caption('Ping pongg')
SIZE = (600, 600)
canvas = pygame.display.set_mode(SIZE)
BG_COLOR = (252, 16, 140)
clock = pygame.time.Clock()
ball_img = pygame.image.load('D:/CS15/Buoi13/assets/ball.png')
paddle_img = pygame.image.load('D:/CS15/Buoi13/assets/paddle.png')

paddle_1_x = 0
paddle_1_y = 250
paddle_2_x = 570
paddle_2_y = 250
ball_x = 285
ball_y = 300
# setup bien danh cho nut bam
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
# speed
speed_x = 1.5
speed_y = 3.5

loop = True
while loop:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True
            elif e.key == pygame.K_UP:
                up_pressed = True
            elif e.key == pygame.K_DOWN:
                down_pressed = True 
        
        elif e.type == pygame.KEYUP:  # khong nhan phim
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_UP:
                up_pressed = False
            elif e.key == pygame.K_DOWN:
                down_pressed = False
    
    ball_x += speed_x
    ball_y += speed_y

    if ball_x <= (paddle_1_x + 30) and paddle_1_y <= ball_y <= (paddle_1_y + 120):
        speed_x = -speed_x
    if ball_x <= (paddle_2_x + 30) and paddle_1_y <= ball_y <= (paddle_2_y + 120):
        speed_x = -speed_x

    if ball_x <= 0 or ball_x >= 570:
         speed_x = -speed_x
    if ball_y <= 0 or ball_y >= 570:
         speed_y = -speed_y

    if paddle_1_y <= 0:
        w_pressed = False
    if paddle_2_y <=0:
        up_pressed = False
    if paddle_1_y >= 480:
        s_pressed - False
    if paddle_2_y >= 480:
        down_pressed = False

    if w_pressed:
        paddle_1_y -= 5
    elif s_pressed:
        paddle_1_y += 5
    elif up_pressed:
        paddle_2_y -= 5
    elif down_pressed:
        paddle_2_y += 5




    canvas.fill(BG_COLOR)
    canvas.blit(ball_img, (ball_x, ball_y))
    canvas.blit(paddle_img, (paddle_1_x, paddle_1_y))
    canvas.blit(paddle_img, (paddle_2_x, paddle_2_y))
    clock.tick(60)
    pygame.display.flip()

