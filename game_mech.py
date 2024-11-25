
def display_matrix(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Функция для заполнения матрицы 
def initialize_board(): 
    return [[" " for _ in range(3)] for _ in range(3)]

# Функция для проверки заполненности игрового поля
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)