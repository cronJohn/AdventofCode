board = [
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        ]

rightBounds = len(board[0]) - 1 # X
bottomBounds = len(board) - 1 # Y

headLocation = [0,bottomBounds]
tailLocation = [0,bottomBounds]



def isInRange():
    # Check x locations
    if ((headLocation[0] not in range(tailLocation[0] - 1, tailLocation[0] + 2)) or  
    # Check y locations
        (headLocation[1] not in range(tailLocation[1] - 1, tailLocation[0] + 2))):  
            return False

def moveDiagonal(direction):
    # Works under the condition that the head has already moved
    if direction == "U":
        tailLocation = [headLocation[0], headLocation[1] + 1]

    if direction == "D":
        tailLocation = [headLocation[0], headLocation[1] - 1]

    if direction == "L":
        tailLocation = [headLocation[0] + 1, headLocation[1]]

    if direction == "R":
        tailLocation = [headLocation[0] - 1, headLocation[1]]

def moveRegular(direction):
    if direction == "U":
        tailLocation = [headLocation[0], headLocation[1] - 1]

    if direction == "D":
        tailLocation = [headLocation[0], headLocation[1] + 1]

    if direction == "L":
        tailLocation = [headLocation[0] - 1, headLocation[1]]

    if direction == "R":
        tailLocation = [headLocation[0] + 1, headLocation[1]]


def isRegularMove():
    if (((headLocation[0] in range(tailLocation[0] - 2, tailLocation[0] + 2)) and (headLocation[1] == tailLocation[1])) or
        ((headLocation[1] in range(tailLocation[1] - 2, tailLocation[1] + 2)) and (headLocation[0] == tailLocation[0]))):
                return True

def stampOcto():
    board[tailLocation[1]][tailLocation[0]] = "#"

def determineCorrectDirection(direction):
    if isInRange():
        pass # Don't move it
    else:
        if isRegularMove():
            moveRegular(direction)
        else:
            moveDiagonal(direction)
        stampOcto()

def parse(string):
    temp = string.split(" ")

    direction = temp[0]
    amount = int(temp[1])

    print(f'head | x: {headLocation[0]} y: {headLocation[1]}')
    print(f'tail | x: {tailLocation[0]} y: {tailLocation[1]}')

    move(amount, direction)

    print(f'head | x: {headLocation[0]} y: {headLocation[1]}')
    print(f'tail | x: {tailLocation[0]} y: {tailLocation[1]}')

def move(amount, direction):
    print(f'moving {direction} by {amount} units')
    for i in range(0, amount):
        if direction == "U":
            headLocation[1] += 1

        if direction == "D":
            headLocation[1] -= 1

        if direction == "L":
            tailLocation[0] -= 1

        if direction == "R":
            tailLocation[0] += 1

        determineCorrectDirection(direction)

stampOcto()

with open('day9-input.txt','r') as inputObj:
        line = inputObj.readline().strip()

        while line:
            for deal in board:
                print(deal)
            parse(line)
            line = inputObj.readline().strip()

print(board)

