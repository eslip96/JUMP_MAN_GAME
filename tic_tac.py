def get_winner(board):
    winning_combo = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for a, b, c in winning_combo:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]
    return ''


board1 = ['X', '', 'X', 'O', 'O', '', '', 'X', 'O']
print(get_winner(board1) == '')

board2 = ['X', '', 'X', 'O', 'O', 'O', 'X', 'X', 'O']
print(get_winner(board2) == 'O')

board3 = ['X', '', 'X', 'X', 'O', 'O', 'X', '', 'O']
print(get_winner(board3) == 'X')

board4 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']
print(get_winner(board4) == 'X')

board5 = ['', '', '', '', 'O', '', 'X', '', '']
print(get_winner(board5) == '')
