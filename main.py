import pygame
import sys
import chess
import json

pygame.init()
board = chess.Board()

WIDTH = 480

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Chess")
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
background_play = pygame.image.load("images/background_play.png").convert()
font_path = "font/KdamThmorPro-Regular.ttf"
font = pygame.font.Font(font_path, 24)
screen = pygame.display.set_mode((840, 480))


def render_piece_count(win, piece_counts, x, y):
    piece_texts = [f"{piece}: {count}" for piece, count in piece_counts.items()]
    for i, piece_text in enumerate(piece_texts):
        text_surface = font.render(piece_text, True, WHITE)
        win.blit(text_surface, (x, y + i * 30))


def count_pieces(board):
    piece_counts = {"P": 0, "N": 0, "B": 0, "R": 0, "Q": 0, "K": 0,
                    "p": 0, "n": 0, "b": 0, "r": 0, "q": 0, "k": 0}

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            piece_counts[piece.symbol()] += 1

    total_counts = {"White": sum(piece_counts[piece] for piece in ["P", "N", "B", "R", "Q", "K"]),
                    "Black": sum(piece_counts[piece] for piece in ["p", "n", "b", "r", "q", "k"])}

    return total_counts


def render_text(win, text, x, y):
    text_surface = font.render(text, True, WHITE)
    win.blit(text_surface, (x, y))
