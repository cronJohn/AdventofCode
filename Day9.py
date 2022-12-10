headLocation = [0,0]
tailLocation = [0,0]

moves = {
        "D": [0,-1],
        "U": [0, 1],
        "L": [-1, 0],
        "R": [1, 0]
}

knots = [[0,0] for _ in range(10)]

previousLocations = set()

def inRange():
    return abs(headLocation[0] - tailLocation[0]) <= 1 and abs(headLocation[1] - tailLocation[1]) <= 1

def inRangeArb(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def addPreviousLocation():
    #previousLocations.add((tailLocation[0], tailLocation[1]))
    previousLocations.add(tuple(knots[-1]))

def parse(string):
    temp = string.split(" ")

    direction = temp[0]
    amount = int(temp[1])

    dx, dy = moves[direction]
    
    for _ in range(amount):
        move(dx,dy)
        #addPreviousLocation()
        addPreviousLocation()

def move(dx, dy):
    global headLocation, tailLocation, knots

    # Update first knot in knots
    knots[0][0] += dx
    knots[0][1] += dy

    #headLocation[0] += dx
    #headLocation[1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not inRangeArb(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            #sign_x = 0 if headLocation[0] == tailLocation[0] else (headLocation[0] - tailLocation[0]) / abs(headLocation[0] - tailLocation[0])
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
            #sign_y = 0 if headLocation[1] == tailLocation[1] else (headLocation[1] - tailLocation[1]) / abs(headLocation[1] - tailLocation[1])

            tx += sign_x
            ty += sign_y

            #tailLocation[0] += sign_x
            #tailLocation[1] += sign_y

        knots[i] = [tx, ty]

with open('day9-input.txt','r') as inputObj:
        line = inputObj.readline().strip()

        while line:
            parse(line)
            line = inputObj.readline().strip()

print(len(previousLocations))

