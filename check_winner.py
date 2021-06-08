def winner(board, char):
    start = 1
    end = 10
    for i in range(start, end):
        if((i == 1 or i == 4 or i == 7) and (board[str(i)] == board[str(i+1)] == board[str(i+2)] == char)):
            return True, board[str(i)]
        if ((i ==1 or i==2 or i==3) and (board[str(i)] == board[str(i+3)] == board[str(i+6)] == char)):
            return True, board[str(i)]
        if i == 1 and board[str(i)] == board[str(i+4)] == board[str(i+8)] == char:
            return True, board[str(i)]
        if i == 3 and board[str(i)] == board[str(i + 2)] == board[str(i + 4)] == char:
            return True, board[str(i)]
    return False, 'tie'
