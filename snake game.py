import pygame
import random

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

font_style = pygame.font.SysFont('Arial',20)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [20, 20])

def dis_score(score, color):
    ur_score = font_style.render('score: ' + str(score), True, color)
    dis.blit(ur_score, [500,500])

dis_dim = 600

dis=pygame.display.set_mode((dis_dim, dis_dim))
pygame.display.set_caption('Snake game by Yuwei Zhu')
pygame.display.update()

def game_loop():
    grow = False
    snake_line = []
    score = 0

    x = dis_dim/2
    y = dis_dim/2
    x_move = 0
    y_move = 0

    clock = pygame.time.Clock()

    snake_block = 20
    snake_speed = 15

    game_close = False
    game_over = False

    foodx = 40
    foody = 40

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", blue)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -snake_block
                    y_move = 0
                elif event.key == pygame.K_RIGHT:
                    x_move = snake_block
                    y_move = 0
                elif event.key == pygame.K_UP:
                    x_move = 0
                    y_move = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_move = 0
                    y_move = snake_block
        if x <= 0 or x >= dis_dim or y < 0 or y >=dis_dim:
            game_close = True



        x += x_move
        y += y_move

        snake_bod = []
        snake_bod.append(x)
        snake_bod.append(y)
        snake_line.append(snake_bod)

        rep = 0
        dis.fill(white)

        for i in snake_line:
            pygame.draw.rect(dis, blue, [i[0], i[1], snake_block, snake_block])
            rep += 1
            if i == snake_line[0] and len(snake_line) > 1 and rep > 1:
                game_close = True



        if grow is False:
            snake_line.pop(0)

        grow = False

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        dis_score(score, green)
        pygame.display.update()
        clock.tick(snake_speed)

        if x == foodx and y == foody:
            print('yummy')
            foodx = random.randrange(1, 20) * 20.0
            foody = random.randrange(1, 25) * 20.0
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            score = score + 1
            grow = True





    pygame.quit()
    quit()
game_loop()
