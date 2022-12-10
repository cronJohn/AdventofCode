headLocation = [0,0]
tailLocation = [0,0]

moves = {
        "D": [0,-1],
        "U": [0, 1],
        "L": [-1, 0],
        "R": [1, 0]
}

previousLocations = set()

def inRange():
    return abs(headLocation[0] - tailLocation[0]) <= 1 and abs(headLocation[1] - tailLocation[1]) <= 1

def addPreviousLocation():
    previousLocations.add((tailLocation[0], tailLocation[1]))

def parse(string):
    temp = string.split(" ")

    direction = temp[0]
    amount = int(temp[1])

    dx, dy = moves[direction]
    
    for _ in range(amount):
        move(dx,dy)
        addPreviousLocation()

def move(dx, dy):
    global headLocation, tailLocation

    headLocation[0] += dx
    headLocation[1] += dy

    if not inRange():
        sign_x = 0 if headLocation[0] == tailLocation[0] else (headLocation[0] - tailLocation[0]) / abs(headLocation[0] - tailLocation[0])
        sign_y = 0 if headLocation[1] == tailLocation[1] else (headLocation[1] - tailLocation[1]) / abs(headLocation[1] - tailLocation[1])

        tailLocation[0] += sign_x
        tailLocation[1] += sign_y

with open('day9-input.txt','r') as inputObj:
        line = inputObj.readline().strip()

        while line:
            parse(line)
            line = inputObj.readline().strip()

print(len(previousLocations))

