#функция, которая принимает в себя матрицу и, если в этой матрице три одинаковых символа идут подряд
#(вертикально, горизонтально или по диагонали), то выводится этот символ, иначе выводится False.
def check_winner(matrix):
    for gor in range(3):   # Проверка горизонтальных линий
        if matrix[gor][0] == matrix[gor][1] == matrix[gor][2] and matrix[gor][0] != '':
            return matrix[gor][0]

    for ver in range(3):   # Проверка вертикальных линий
        if matrix[0][ver] == matrix[1][ver] == matrix[2][ver] and matrix[0][ver] != '':
            return matrix[0][ver]

    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '':      # Проверка диагоналей
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != '':
        return matrix[0][2],

    return False

matrix = [              #пример
    ['o', '', 'x'],
    ['x', 'x', 'x'],
    ['o', 'o', '']
]

result = check_winner(matrix)
print(result)
