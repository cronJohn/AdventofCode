arr = []
total = 0

def checkBounds(x,y):
    flag = 0 # 0 means clear >= 1 means blocked

    # Check row
    for x_it in range(x_start-1, x_end+1):
        if x != x_it: 
            if (arr[y][0][x_it] >= arr[y][0][x]):
                flag += 1
        else:
            if flag == 0:
                return 1

            else:
                flag = 0

    if flag == 0:
        return 1

    flag = 0 # Reset flag

    # Check col
    for y_it in range(y_start-1, y_end+1):
        if y != y_it: 
            if (arr[y_it][0][x] >= arr[y][0][x]):
                flag += 1
        else:
            if flag == 0:
                return 1
            else:
                flag = 0

    if flag == 0:
        return 1
    else:
        return 0

def calcScenicScore(x,y):
    total = 1
    temp = 0

    # Check row mid to left
    for x_it in range(x, x_start-2, -1):
        if x != x_it: 
            if (arr[y][0][x_it] < arr[y][0][x]):
                temp += 1
            else:
                temp += 1
                break

    total = temp
    temp = 0

    # Check row mid to right
    for x_it in range(x, x_end+1):
        if x != x_it: 
            if (arr[y][0][x_it] < arr[y][0][x]):
                temp += 1
            else:
                temp += 1
                break

    total *= temp
    temp = 0

    # Check col mid to top
    for y_it in range(y, y_start-2, -1):
        if y != y_it: 
            if (arr[y_it][0][x] < arr[y][0][x]):
                temp += 1
            else:
                temp += 1
                break

    total *= temp
    temp = 0


    # Check col mid to bottom
    for y_it in range(y, y_end+1):
        if y != y_it: 
            if (arr[y_it][0][x] < arr[y][0][x]):
                temp += 1
            else:
                temp += 1
                break
    total *= temp

    return total


with open('day8-input.txt','r') as inputObj:
        line = inputObj.readline().strip()
        while line:
            arr.append([line])
            line = inputObj.readline().strip()

x_start = 1
x_end = len(arr[0][0]) - 1
y_start = 1
y_end = len(arr) - 1
perimeter_trees = (2*(x_end+1+y_end+1))-4
deal = []

for row in range(y_start, y_end):
    for col in range(x_start, x_end):
        #total += checkBounds(col, row)
        deal.append(calcScenicScore(col,row))

print(max(deal))
#print(f'total {total + perimeter_trees}')

