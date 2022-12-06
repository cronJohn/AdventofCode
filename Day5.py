craneBoardArr = []

def getTidiedRows(num):
    tidiedRows = []
    num = int(num)
    end = ((num*3)+(num-1))-2 # Includes letter spaces(which is 3 wide) + separator spaces(which is 1 wide)

    for row in craneBoardArr:
        start = 0
        finished = False
        temp = []
        while not finished:
            if row[start:start+3].strip() == "": # Must add strip which fixes an issue if there are spaces after the last letter
                temp.append('⨯')
            else:
                temp.append(row[start+1:start+2])
            start += 4
            if start > end:
                finished = True 

        tidiedRows.append(temp)

    return tidiedRows 

def getNumberOfCols(string):
    temp = string.split('   ')
    return max(temp)

def getColumn(array, index):
    return [row[index] for row in array]

numberOfCols = 0
with open('day5-input.txt','r') as inputObj:
        line = inputObj.readline()
        while line: # Looping until number row at the bottom
            line = str(line.strip())
            print(line)
            
            if any(chr.isdigit() for chr in line):
                numberOfCols = getNumberOfCols(line)
                break

            else:
                craneBoardArr.append(line)

            line = inputObj.readline()

        tidiedRows = getTidiedRows(numberOfCols)
        craneColumns = []

        for i in range(0, len(tidiedRows)):
            craneColumns.append(getColumn(tidiedRows, i)) # Convert columns to rows

        for i in range(0, len(craneColumns)):
            craneColumns[i] = [x for x in craneColumns[i] if x != "⨯"] # Remove placeholder ⨯

        for col in craneColumns:
            print(col)

