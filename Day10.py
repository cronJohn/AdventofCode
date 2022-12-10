currentCycle = 0
register = 1

cyclesBoard = []
crt = ['.'] * 241

# Second part inspiration | https://www.youtube.com/watch?v=yusuO0FDB28

def parse(string):
    global currentCycle, register, deal, cyclesBoard
    temp = string.split(" ")

    command = temp[0]
    
    if len(temp) == 1:
        amount = None
    else:
        amount = int(temp[1])

    if command == "noop":
        cyclesBoard.append(register)

        #currentCycle += 1

        #if currentCycle in targets:
            #deal.append(currentCycle * register)

    elif command == "addx":
        cyclesBoard.append(register)
        cyclesBoard.append(register)
        register += amount

        #register += amount

        #for _ in range(0,2):
            #currentCycle += 1
            #if currentCycle in targets:
                #deal.append(currentCycle * (register - amount))

deal = []
targets = [20,60,100,140,180,220]

with open('day10-input.txt','r') as inputObj:
        line = inputObj.readline().strip()

        while line:
            parse(line)
            
            line = inputObj.readline().strip()

for row in range(0, len(cyclesBoard), 40):
    for col in range(40):
        print("#" if abs(cyclesBoard[row + col] - col) <= 1 else " ", end = "")
    print()


#print(f'sum of all is {sum(deal)}')
