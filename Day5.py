craneBoardArr = []

with open('day5-input.txt','r') as inputObj:
        line = inputObj.readline()
        while line:
            line = str(line.strip())
            print(line)
            
            if any(chr.isdigit() for chr in line):
                print('stop')
                break

            else:
                craneBoardArr.append(line)

            line = inputObj.readline()

tidiedRows = []
start = 0
finished = False
print(f'crane board: {craneBoardArr}')
for row in craneBoardArr:
    while not finished:
        print(f'starting deal: {row[start:start+3]}')
        if row[start:start+3] == "   ":
            tidiedRows.append('⨯')
        else:
            tidiedRows.append(row[start+1:start+2])

        start += 4

        if start > 35:
            finished = True 

    finished = False
    start = 0
    print('--------------------------------')

print(f'new array: {tidiedRows}')
