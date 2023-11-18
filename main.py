import pygame
import sys
import chess
import json

class Node:
    def init(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(col * width)
        self.y = int(row * width)
        self.colour = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, win, boardM):

        if boardM[self.row][self.col] != "None":
            win.blit(pygame.image.load(self.get_image(boardM[self.row][self.col])), (self.x, self.y))

    @staticmethod
    def get_image(letter):
        if letter == 'r':
            return "images/b_tower.png"
        if letter == 'n':
            return "images/b_horse.png"
        if letter == 'b':
            return "images/b_bishop.png"
        if letter == 'q':
            return "images/b_queen.png"
        if letter == 'k':
            return "images/b_king.png"
        if letter == 'p':
            return "images/b_rook.png"

        if letter == 'R':
            return "images/w_tower.png"
        if letter == 'N':
            return "images/w_horse.png"
        if letter == 'B':
            return "images/w_bishop.png"
        if letter == 'Q':
            return "images/w_queen.png"
        if letter == 'K':
            return "images/w_king.png"
        if letter == 'P':
            return "images/w_rook.png"

        return ""
[19:00]
def make_grid(rows):
    grid = []
    gap = WIDTH // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node)
            if (i + j) % 2 == 1:
                grid[i][j].colour = GREY
    return grid


def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


def update_display(win, grid, rows, width):
    board_m = []
    for i in range(8):
        arr = [str(board.piece_at(chess.Square((i * 8 + j)))) for j in range(8)]
        board_m.insert(0, arr)

    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.setup(win, board_m)
    draw_grid(win, rows, width)
    pygame.display.update()


def find_node(pos, width):
    interval = width / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    x, y = int(rows), int(columns)
    pos = "" + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][x] + f"{8 - y}"
    return pos


def machine_move(boardCopy, depth):
    max = -99999
    movement = ""
    legal_moves = [str(mov) for mov in boardCopy.legal_moves]
    for move in legal_moves:
        result = alphabeta_pruning(boardCopy.copy(), move, depth, -999999, 9999999, False)
        if result > max:
            movement = move
            max = result
    return movement
