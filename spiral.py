def spiralize(size):
    spiral = [[0] * size for i in range(size)]

    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while top <= bottom and left <= right:
        ''' Заполняем верхний ряд слева направо '''
        for i in range(left, right + 1):
            spiral[top][i] = 1

        ''' Заполняем правый ряд сверху вниз '''
        for i in range(top, bottom + 1):
            spiral[i][right] = 1

        ''' Заполняем нижний ряд справо налево '''
        for i in range(right, left -1 , -1):
            spiral[bottom][i]= 1

        ''' Заполняем левый ряд снизу вверх '''
        for i in range(bottom, top - 1, -1):
            if i > top + 1:
                spiral[i][left] = 1

        top += 2
        bottom -= 2
        left += 2
        right -= 2
        if left <= right and top <= bottom:
            spiral[top][left - 1] = 1

    return spiral


spiral = spiralize(5)
for row in spiral:
    print(row)
