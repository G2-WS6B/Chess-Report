positions_evaluated = 0


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

