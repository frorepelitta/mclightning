import random

def display_matrix(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def tic_tac_toe():
    # Инициализируем пустую матрицу 3x3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice(["O", "X"]) #первый игрок

    for turn in range(9):  # Всего 9 ходов
        display_matrix(board)
        print(f"Игрок {current_player}, ваш ход.")

        # Вводим координаты строки и столбца
        row = int(input("Введите номер строки (1, 2 или 3): ")) - 1
        stolb = int(input("Введите номер столбца (1, 2 или 3): ")) -1

        # Проверяем, что введенные координаты находятся в допустимых пределах и место свободно
        if 0 <= row < 4 and 0 <= stolb < 4 and board[row][stolb] == " ":
            board[row][stolb] = current_player
        else:
            print("Недопустимый ход, попробуйте еще раз.")
            continue

        # Переключаем текущего игрока
        current_player = "X" if current_player == "O" else "O"

    display_matrix(board)
    print("Игра завершена!")

tic_tac_toe()
