board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def print_board(layout):
    for i in range(3):
        print(' | '.join(layout[i]))

def get_move(board):
    while True:
        r = int(input('enter row (0-2): '))
        c = int(input('enter column (0-2): '))

        if r in range(3) and c in range(3) and board[r][c] == '_':
            return r, c
        else:
            print('invalid input')

def make_move(board, r, c, player):
    board[r][c] = player

def winner(board, player):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return False

    return True

player = 'X'
while True:
    print_board(board)
    move = get_move(board)
    make_move(board, move[0], move[1], player)

    if winner(board, player):
        print(player + ' won')
        break
    if draw(board):
        print('its a draw')
        break

    player = 'O' if player == 'X' else 'X'
