import pygame
import os
from pygame.locals import *
import math
from Pieces import *
from pygame.constants import (
    MOUSEBUTTONDOWN, MOUSEBUTTONUP
)

pygame.init()

light_square = (255, 255, 255)
dark_square = (139, 69, 19)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (169, 169, 169)
transparent = (0, 0, 0, 0)


#Make Board
board_width=480
margin=30
board_height=board_width
board = pygame.display.set_mode((board_width+margin, board_height+margin))
board.fill(white)
cols=[light_square, dark_square]
sq_dim=board_width/8

for i in range(0,8):
    for j in range(0,8):
        sq_col=cols[(i+j)%2]
        pygame.draw.rect(board, sq_col, ((i*sq_dim), (j*sq_dim), sq_dim, sq_dim))

label_font=pygame.font.SysFont("calibri", 18)

for i in range(0,8):
    #pygame.draw.line(board, grey, (board_width, (i+1)*sq_dim), (board_width+margin, (i+1)*sq_dim), 2)
    #pygame.draw.line(board, grey, ((i+1)*sq_dim, board_height), ((i+1)*sq_dim, board_height+margin), 2)
    col_text=label_font.render(chr(ord('a')+i), True, black)
    row_text=label_font.render(str(8-i), True, black)
    board.blit(col_text, ((i*sq_dim)+22, board_height+8))
    board.blit(row_text, ((board_width+10), (i*sq_dim)+22))
pygame.draw.lines(board, black, True, [(0,0), (board_width, 0), (board_width, board_height), (0, board_height)], 2)
pygame.display.flip()


#Draw Pieces
def pieces():
    board.blit(brook1,brook1_rect)
    board.blit(brook2,brook2_rect)
    board.blit(wrook1,wrook1_rect)
    board.blit(wrook2,wrook2_rect)
    board.blit(bbishop1,bbishop1_rect)
    board.blit(bbishop2,bbishop2_rect)
    board.blit(wbishop1,wbishop1_rect)
    board.blit(wbishop2,wbishop2_rect)
    board.blit(bqueen,bqueen_rect)
    board.blit(wqueen,wqueen_rect)
    board.blit(bknight1,bknight1_rect)
    board.blit(bknight2,bknight2_rect)
    board.blit(wknight1,wknight1_rect)
    board.blit(wknight2,wknight2_rect)
    board.blit(bking,bking_rect)
    board.blit(wking,wking_rect)
    board.blit(bpawn1, bpawn1_rect)
    board.blit(bpawn2, bpawn2_rect)
    board.blit(bpawn3, bpawn3_rect)
    board.blit(bpawn4, bpawn4_rect)
    board.blit(bpawn5, bpawn5_rect)
    board.blit(bpawn6, bpawn6_rect)
    board.blit(bpawn7, bpawn7_rect)
    board.blit(bpawn8, bpawn8_rect)
    board.blit(wpawn1, wpawn1_rect)
    board.blit(wpawn2, wpawn2_rect)
    board.blit(wpawn3, wpawn3_rect)
    board.blit(wpawn4, wpawn4_rect)
    board.blit(wpawn5, wpawn5_rect)
    board.blit(wpawn6, wpawn6_rect)
    board.blit(wpawn7, wpawn7_rect)
    board.blit(wpawn8, wpawn8_rect)


selected_pos = [(0,0)]
p = 0


turnvar = True
running  = True

while running:
    for event in pygame.event.get():
        for i in range(0, 8):
            for j in range(0, 8):
                sq_col = cols[(i + j) % 2]
                pygame.draw.rect(board, sq_col, ((i * sq_dim), (j * sq_dim), sq_dim, sq_dim))

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            pass
        elif event.type == MOUSEBUTTONUP:
            turnvar = turn(selected_pos,p)
            selected_pos.append(nearest_center(pygame.mouse.get_pos()))
            p += 1


            # rooks
            if selected_pos[p - 1] == brook1_rect.center:
                if 'brook1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_rook(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),selected_pos,p) == True:
                        brook1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == brook2_rect.center:
                if 'brook2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_rook(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),selected_pos,p) == True:
                        brook2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wrook1_rect.center:
                if 'wrook1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_rook(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),selected_pos,p) == True:
                        wrook1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wrook2_rect.center:
                if 'wrook2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_rook(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),selected_pos,p) == True:
                        wrook2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            # bishops
            if selected_pos[p - 1] == bbishop1_rect.center:
                if 'bbishop1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bishop(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                         selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bbishop1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bbishop2_rect.center:
                if 'bbishop2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bishop(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                         selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bbishop2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wbishop1_rect.center:
                if 'wbishop1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bishop(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                         selected_pos[p - 1], selected_pos[p],selected_pos,p) == True:
                        wbishop1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wbishop2_rect.center:
                if 'wbishop2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bishop(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                         selected_pos[p - 1], selected_pos[p],selected_pos,p) == True:
                        wbishop2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            # queens
            if selected_pos[p - 1] == bqueen_rect.center:
                if 'bqueen' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_queen(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p - 1], selected_pos[p],selected_pos,p) == True:
                        bqueen_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wqueen_rect.center:
                if 'wqueen' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_queen(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p - 1], selected_pos[p],selected_pos,p) == True:
                        wqueen_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            # knights
            if selected_pos[p - 1] == bknight1_rect.center:
                if 'bknight1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_knight(selected_pos[p - 1], selected_pos[p],selected_pos,p) == True:
                        bknight1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bknight2_rect.center:
                if 'bknight2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_knight(selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bknight2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wknight1_rect.center:
                if 'wknight1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_knight(selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wknight1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wknight2_rect.center:
                if 'wknight2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_knight(selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wknight2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            # kings
            if selected_pos[p - 1] == bking_rect.center:
                if 'bking' in capturedpieces:
                    print('GAME OVER!!! WHITE WINS!!!')
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_king(selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bking_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wking_rect.center:
                if 'wking' in capturedpieces:
                    print('GAME OVER!!! BLACK WINS!!!')
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_king(selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wking_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            # pawns
            if selected_pos[p - 1] == bpawn1_rect.center:
                if 'bpawn1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn2_rect.center:
                if 'bpawn2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn3_rect.center:
                if 'bpawn3' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn3_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn4_rect.center:
                if 'bpawn4' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn4_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn5_rect.center:
                if 'bpawn5' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn5_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn6_rect.center:
                if 'bpawn6' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn6_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn7_rect.center:
                if 'bpawn7' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn7_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == bpawn8_rect.center:
                if 'bpawn8' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_bpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        bpawn8_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn1_rect.center:
                if 'wpawn1' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn1_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn2_rect.center:
                if 'wpawn2' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn2_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn3_rect.center:
                if 'wpawn3' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn3_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn4_rect.center:
                if 'wpawn4' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn4_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn5_rect.center:
                if 'wpawn5' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn5_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn6_rect.center:
                if 'wpawn6' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn6_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn7_rect.center:
                if 'wpawn7' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn7_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

            if selected_pos[p - 1] == wpawn8_rect.center:
                if 'wpawn8' in capturedpieces:
                    selected_pos.append((0, 0))
                    p += 1
                elif turnvar == True:
                    if valid_move_wpawn(position_name(selected_pos[p - 1]), position_name(selected_pos[p]),
                                        selected_pos[p-1],selected_pos[p],selected_pos,p) == True:
                        wpawn8_rect.center = selected_pos[p]
                        selected_pos.append((0, 0))
                        p += 1

        pieces()
        pygame.display.update()

pygame.quit()
