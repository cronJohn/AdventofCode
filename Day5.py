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

print(f'crane board: {craneBoardArr}')
rows = []
for row in craneBoardArr:
    temp = row.split(' ')

    rows.append(temp)
    print(f'row length: {len(temp)}')
    print(f'row: "{row}"')

print(f'new array: {rows}')
