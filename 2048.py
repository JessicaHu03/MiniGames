# Python 2048 Project.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

matrix = [[0 for o in range(4)] for l in range(4)]
score = 0


########################################## DISPLAY ################################################


def ifZero(s: matrix) -> str:
    """
    Check if the parameter s is 0 and handle the so case
    If the parameter s is 0, return empty string, otherwise return s
    """
    return s if s != 0 else ''


def display():
    """
    Display the 4x4 matrix
    """
    print(' \033[1;37;40m Welcome to Mini 2048 \033[0m')
    print('\r'
          '------- ------ ------ -------\n'
          '| %4s | %4s | %4s | %4s |\n'
          '|------ ------ ------ ------|\n'
          '| %4s | %4s | %4s | %4s |\n'
          '|------ ------ ------ ------|\n'
          '| %4s | %4s | %4s | %4s |\n'
          '|------ ------ ------ ------|\n'
          '| %4s | %4s | %4s | %4s |\n'
          '|------ ------ ------ ------|'
          % (ifZero(matrix[0][0]), ifZero(matrix[0][1]),
             ifZero(matrix[0][2]), ifZero(matrix[0][3]),
             ifZero(matrix[1][0]), ifZero(matrix[1][1]),
             ifZero(matrix[1][2]), ifZero(matrix[1][3]),
             ifZero(matrix[2][0]), ifZero(matrix[2][1]),
             ifZero(matrix[2][2]), ifZero(matrix[2][3]),
             ifZero(matrix[3][0]), ifZero(matrix[3][1]),
             ifZero(matrix[3][2]), ifZero(matrix[3][3]),)
          )
    print('\033[1;37;40m score:%s \033[0m' % score)


def init():
    initNumFlag = 0
    while True:
        k = 2 if random.randrange(0, 10) > 1 else 4  # randomly generate 2 and 4
        s = divmod(random.randrange(0, 16), 4)  #
        if matrix[s[0]][s[1]] == 0:  # give value when its value is not 0 to avoid repeat values
            matrix[s[0]][s[1]] = k
            initNumFlag += 1
            if initNumFlag == 2:
                break
    display()


####################################### UP DOWN LEFT RIGHT #########################################

def moveRight():
    """
    Start Traversing from the upper right corner
    """
    global score
    for i in range(4):  # i controls rows
        for j in range(3, 0, -1):  # j controls columns
            for k in range(j - 1, -1, -1):  # k controls the first j-1 values in i rows
                if matrix[i][k] > 0:  # current tile has an value to be sum up
                    if matrix[i][j] == 0:  # right most tile is 0
                        if k > 0 and matrix[i][k] == matrix[i][k - 1]:
                            # when k tile is not the first tile and two adjacent values is the same
                            matrix[i][k] *= 2
                            score += matrix[i][k]  # add the current value to score
                            matrix[i][k - 1] = 0
                        if k == j - 1 and matrix[i][k - 1] == 0 and matrix[i][k] == matrix[i][
                            k - 2]:
                            # when there is a zero in between two same values
                            matrix[i][k] *= 2
                            score += matrix[i][k]
                            matrix[i][k - 2] = 0
                        matrix[i][j] = matrix[i][k]  # move the sum to the right most tile
                        matrix[i][k] = 0  # set original tile to 0
                    elif matrix[i][j] == matrix[i][k]:  # two right most adjacent values
                        matrix[i][j] *= 2
                        score += matrix[i][j]
                        matrix[i][k] = 0
                    break


def moveLeft():
    """
    Start Traversing from the Upper left corner
    """
    global score
    for i in range(4):  # i controls rows
        for j in range(4):  # j controls columns
            for k in range(j+1, 4, 1):  # k controls the first j+1 values in i rows
                if matrix[i][k] > 0:  # current tile has an value to be sum up
                    if matrix[i][j] == 0:  # left most tile is 0
                        if k < j and matrix[i][k] == matrix[i][k + 1]:
                            # when k tile is not the last tile and two adjacent values is the same
                            # (in the middle)
                            matrix[i][k] *= 2
                            score += matrix[i][k]  # add the current value to score
                            matrix[i][k + 1] = 0
                        if k == 1 and matrix[i][k + 1] == 0 and matrix[i][k] == matrix[i][k + 2]:
                            # when there is a zero in between two same values
                            matrix[i][k] *= 2
                            score += matrix[i][k]
                            matrix[i][k + 2] = 0
                        matrix[i][j] = matrix[i][k]  # move the sum to the left most tile
                        matrix[i][k] = 0  # set original tile to 0
                    elif matrix[i][j] == matrix[i][k]:  # two left most adjacent values
                        matrix[i][j] *= 2
                        score += matrix[i][j]
                        matrix[i][k] = 0
                    break


def moveUp():
    """
    Start Traversing from the Bottom right corner
    """
    global score
    for i in range(3, 0, -1):  # i controls rows
        for j in range(3, 0, -1):  # j controls columns
            for k in range(i-1, -1, -1):  # k controls the last i-1 values in j column
                if matrix[k][j] > 0:  # current tile has an value to be sum up
                    if matrix[i][j] == 0:  # up most tile is 0
                        if k < i and matrix[k][j] == matrix[k + 1][j]:
                            # when k is not the last tile and two adjacent values is the same
                            # (in the middle)
                            matrix[k][j] *= 2
                            score += matrix[k][j]  # add the current value to score
                            matrix[k + 1][j] = 0
                        if k == 1 and matrix[k + 1][j] == 0 and matrix[k][j] == matrix[k + 2][j]:
                            # when there is a zero in between two same values
                            matrix[k][j] *= 2
                            score += matrix[k][j]
                            matrix[k + 2][j] = 0
                        matrix[i][j] = matrix[k][j]  # move the sum to the up most tile
                        matrix[k][j] = 0  # set original tile to 0
                    elif matrix[i][j] == matrix[k][j]:  # two up most adjacent values
                        matrix[i][j] *= 2
                        score += matrix[i][j]
                        matrix[k][j] = 0
                    break


def moveDown():
    """
    Start traversing from the Bottom left corner
    :return:
    """
    global score
    for i in range(3, 0, -1):  # i controls rows
        for j in range(4):  # j controls columns
            for k in range(i - 1, -1, -1):  # k controls the first i-1 values in j rows
                if matrix[k][j] > 0:  # current tile has an value to be sum up
                    if matrix[i][j] == 0:  # down most tile is 0
                        if k > 0 and matrix[k][j] == matrix[k - 1][j]:
                            # when k tile is not the first tile and two adjacent values is the same
                            matrix[k][j] *= 2
                            score += matrix[k][j]  # add the current value to score
                            matrix[k - 1][j] = 0
                        if k == i - 1 and matrix[k - 1][j] == 0 and matrix[k][j] == matrix[k - 2][
                            j]:
                            # when there is a zero in between two same values
                            matrix[k][j] *= 2
                            score += matrix[k][j]
                            matrix[k - 2][j] = 0
                        matrix[i][j] = matrix[k][j]  # move the sum to the down most tile
                        matrix[k][j] = 0  # set original tile to 0
                    elif matrix[i][j] == matrix[k][j]:  # two down most adjacent values
                        matrix[i][j] *= 2
                        score += matrix[i][j]
                        matrix[k][j] = 0
                    break


####################################Automatic Game System##########################################


def addRandomNum():
    """
    add random 2 or 4 at places not 0 after player take the move and re-display
    """
    while True:
        k = 2 if random.randrange(0, 10) > 1 else 4
        s = divmod(random.randrange(0, 16), 4)
        if matrix[s[0]][s[1]] == 0:
            matrix[s[0]][s[1]] = k
            break
    display()


def checkOver():
    """"
    Traversing every element in the matrix
    If there exists a value 0 (empty tile) or a value that can be added up with surrounding values,
    the game is not over, return False, else game Over, return True
    """
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == 0 or matrix[i][j] == matrix[i][j + 1] or matrix[j][i] == \
                    matrix[j + 1][i]:
                return False
        else:
            return True


def main():
    flag = True
    init()
    while flag:
        d = input('\033[1;36;1m W:Up S: Down A:Left D: Right Q: Quit :\033[0m')
        if d == 'A':  # move left
            moveLeft()
        elif d == 'S':
            moveDown()
        elif d == 'W':
            moveUp()
        elif d == 'D':
            moveRight()
        elif d == 'Q':
            break
        else:  # for other inputs, do nothing
            continue
        addRandomNum()
        if checkOver():
            print('GAME OVER')
            flag = False


if __name__ == '__main__':
    main()
