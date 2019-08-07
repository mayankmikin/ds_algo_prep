    # WRITE YOUR CODE HERE


def removeObstacle(numRows, numColumns, lot):
    if numRows <= 1 or numColumns >= 1000 or numColumns < 1:
        return -1
    for row in range(numRows):
        for col in range(numColumns):
          if lot[row][col] == 9:
            return row + col
    return -1


if __name__ == '__main__':
    print '##### Edge cases ######'
    print 'Output: ', removeObstacle(1, 1, [[9]])
    print 'Output: ', removeObstacle(0, 0, [[]])

    print '\n##### Input: 1 ######'
    m = 3
    n = 3
    l = [
          [1, 0, 0],
          [1, 0, 0],
          [1, 9, 1]
        ]
    print 'Output: ', removeObstacle(m, n, l)

    print '\n##### Input: 2 ######'
    m = 5
    n = 4
    l = [
          [1, 1, 1, 1],
          [0, 1, 1, 1],
          [0, 1, 0, 1],
          [1, 1, 9, 1],
          [0, 0, 1, 1]
        ]
    print 'Output: ', removeObstacle(m, n, l)
