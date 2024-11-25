from game_mech import display_matrix
from game_mech import initialize_board
from game_mech import is_board_full
from victory_check import check_winner


board = initialize_board()
current_player = "X"

while True:
    display_matrix(board)
    row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
    col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player
    else:
        print("Эта клетка уже занята. Попробуйте снова.")
        continue

    winner = check_winner(board)
    if winner:
        display_matrix(board)
        print(f"Поздравляем, игрок {winner} выиграл!")
        break

    if is_board_full(board):
        display_matrix(board)
        print("Игра окончена вничью!")
        break

    current_player = "O" if current_player == "X" else "X"