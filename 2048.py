import random
import sys
from collections.abc import Iterable
from functools import reduce
import pygame
import math
import numpy as np

score = 0
width, height = (370, 600)
margin_size = 10
block_size = 80

def new_game():
    mat = np.zeros((4, 4))
    mat = add_random_block(mat)
    mat = add_random_block(mat)
    score = 0
    return mat

def add_random_block(mat):
    i = random.randint(0, len(mat) - 1)
    j = random.randint(0, len(mat) - 1)
    while(mat[i][j] != 0):
        i = random.randint(0, len(mat) - 1)
        j = random.randint(0, len(mat) - 1)
    mat[i][j] = random.randint(1, 2) * 2
    return mat

def print_mat(mat):
    for row in mat:
        print(row)

def change_left_right(mat):
    new_mat = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[i][3-j]
    return new_mat

def change_row_column(mat):
    new_mat = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[j][i]
    return new_mat

def compress(mat):
    move_or_not = 0
    new_mat = np.zeros((4, 4))
    for i in range(4):
        index = 0
        for j in range(4):
            if mat[i][j] != 0:
                if index != j:
                    move_or_not = 1
                new_mat[i][index] = mat[i][j]
                index += 1
    return move_or_not, new_mat

def merge(mat):
    global score
    move_or_not = 0
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                move_or_not = 1
                mat[i][j] *= 2
                score += mat[i][j]
                mat[i][j+1] = 0
    return move_or_not, mat

def move_left(mat):
    move_or_not1, mat = compress(mat)
    move_or_not2, mat = merge(mat)
    move_or_not3, mat = compress(mat)
    print(move_or_not1)
    print(move_or_not2)
    print(move_or_not3)
    move_or_not = move_or_not1 or move_or_not2 or move_or_not3 
    print(move_or_not)
    return move_or_not, mat

def move_right(mat):
    mat = change_left_right(mat)
    move_or_not, mat = move_left(mat)
    mat = change_left_right(mat)
    return move_or_not, mat

def move_up(mat):
    mat = change_row_column(mat)
    move_or_not, mat = move_left(mat)
    mat = change_row_column(mat)
    return move_or_not, mat

def move_down(mat):
    mat = change_row_column(mat)
    move_or_not, mat = move_right(mat)
    mat = change_row_column(mat)
    return move_or_not, mat

def gameover_or_not(mat):
    flag = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 0
            elif j + 1 < 4 and mat[i][j] == mat[i][j+1]:
                return 0
            elif i + 1 < 4 and mat[i][j] == mat[i + 1][j]:
                return 0
    return 1

def draw_back(screen):
    for i in range(4):
        for j in range (4):
            x = margin_size * (j + 1) + block_size * j
            y = margin_size * (i + 1) + block_size * i + height - width
            pygame.draw.rect(screen, pygame.Color('#f9f6f2'), (x, y, block_size,block_size))

color_map = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}


def draw_num(screen, mat):
    font_size = block_size - 15
    font = pygame.font.Font(None, font_size)
    for i in range(4):
        for j in range(4):
            if mat[i][j] != 0:
                x = margin_size * (j + 1) + block_size * j 
                y = margin_size * (i + 1) + block_size * i + height - width
                font_color = pygame.Color('#776e65')
                text = font.render(str(int(mat[i][j])), True, font_color)
                rect = text.get_rect()
                rect.centerx, rect.centery = x + block_size / 2, y + block_size / 2
                pygame.draw.rect(screen, pygame.Color(color_map.get(mat[i][j], '#776e65')), (x, y, block_size, block_size))
                screen.blit(text, rect)

def draw_score(screen,score):
    font_size = block_size - 15
    font = pygame.font.Font(None, font_size)

    font_color = pygame.Color('#f9f6f2')
    text = font.render('score:'+str(score), True, font_color)
    screen.blit(text, (25, 25))

def draw_gameover(screen):
    font_size = block_size
    font = pygame.font.Font(None, font_size)

    font_color = pygame.Color('#f9f6f2')
    text = font.render('Gameover.', True, font_color)
    screen.blit(text, (25, 85))

    font_size = block_size -30
    font = pygame.font.Font(None, font_size)
    text = font.render('Press R to restart.', True, font_color)
    screen.blit(text, (25, 150))

def run(screen):
    mat = new_game()
    global score
    clock = pygame.time.Clock()
    gameover = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("Key pressed")
                print(event.key)
                if event.key in [pygame.K_r]:
                    return
                elif event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    direction = {pygame.K_w: 'up', pygame.K_s: 'down', pygame.K_a: 'left', pygame.K_d: 'right'}[event.key]
                    print("press:",direction)
                    move_or_not = 0
                    if direction == "up":
                        move_or_not, mat = move_up(mat)
                    elif direction == "down":
                        move_or_not, mat = move_down(mat)
                    elif direction == "left":
                        move_or_not, mat = move_left(mat)
                        print("test_left")
                    elif direction == "right":
                        move_or_not, mat = move_right(mat)
                    
                    if gameover_or_not(mat) == 1:
                        print("gameover")
                        gameover = 1
                        #pygame.time.delay(2000)

                    if move_or_not == 1:
                        mat = add_random_block(mat)
        


        screen.fill(pygame.Color('#92877d'))

        draw_back(screen)
        
        draw_num(screen, mat)
        
        draw_score(screen,score)

        if gameover:
            draw_gameover(screen)

        pygame.display.flip()
        clock.tick(60)

def main():
    global score
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    while True:
        score = 0
        run(screen)

if __name__ == "__main__":
    main()






 

