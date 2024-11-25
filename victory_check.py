#функция, которая принимает в себя матрицу и, если в этой матрице три одинаковых символа идут подряд
#(вертикально, горизонтально или по диагонали), то выводится этот символ, иначе выводится False.
def check_winner(board):
    # Проверка строк, столбцов и диагоналей на победу
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None


