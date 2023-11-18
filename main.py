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
positions_evaluated = 0

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


def alphabeta_pruning(boardCopy, movement, depth, alpha, beta, maximizingPlayer):
    global positions_evaluated
    if depth == 0:
        return evaluate_board(boardCopy, movement)

    boardCopy.push(chess.Move.from_uci(movement))
    legal_moves = [str(mov) for mov in boardCopy.legal_moves]

    if maximizingPlayer:
        value = -999999
        for move in legal_moves:
            value = max(value, alphabeta_pruning(boardCopy.copy(), move, depth - 1, alpha, beta, False))
            if value >= beta:
                break
            alpha = max(alpha, value)
        return value
    else:
        value = 999999
        for move in legal_moves:
            positions_evaluated += 1
            value = min(value, alphabeta_pruning(boardCopy.copy(), move, depth - 1, alpha, beta, True))
            if value <= alpha:
                break
            beta = min(beta, value)
        return value


def evaluate_board(boardCopy, movement):
    current_board = boardCopy.fen()
    if current_board in evaluated_boards:
        return evaluated_boards[current_board]
    else:
        value = 0
        boardCopy.push(chess.Move.from_uci(movement))
        for i in range(8):
            for j in range(8):
                piece = str(boardCopy.piece_at(chess.Square((i * 8 + j))))
                value += get_value_of_piece(piece)
        evaluated_boards[current_board] = value
        return value


def get_value_of_piece(letter):
    if letter == 'r':
        return 50
    if letter == 'n':
        return 30
    if letter == 'b':
        return 30
    if letter == 'q':
        return 90
    if letter == 'k':
        return 900
    if letter == 'p':
        return 10

    if letter == 'R':
        return -50
    if letter == 'N':
        return -30
    if letter == 'B':
        return -30
    if letter == 'Q':
        return -90
    if letter == 'K':
        return -900
    if letter == 'P':
        return -10

    return 0



