currentCycle = 0
register = 1

def parse(string):
    global currentCycle, register, deal
    temp = string.split(" ")

    command = temp[0]
    
    if len(temp) == 1:
        amount = None
    else:
        amount = int(temp[1])

    if command == "noop":
        currentCycle += 1

        if currentCycle in targets:
            deal.append(currentCycle * register)


    elif command == "addx":
        register += amount

        for _ in range(0,2):
            currentCycle += 1
            if currentCycle in targets:
                deal.append(currentCycle * (register - amount))

deal = []
targets = [20,60,100,140,180,220]

with open('day10-input.txt','r') as inputObj:
        line = inputObj.readline().strip()

        while line:
            parse(line)
            
            line = inputObj.readline().strip()

print(f'sum of all is {sum(deal)}')
