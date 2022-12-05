total = 0

def isCompleteRange(x1, y1, x2, y2):
    
    if (x2 < x1) or (y2 > y1): # Is range2 not fully part of range1
        if (x1 < x2) or (y1 > y2): # Is range1 not fully part of range 2
            return False
    return True

with open('day4-input.txt','r') as inputObj:
        line = inputObj.readline()

        while line:
            temp = []
            word = str(line.strip())
            new = word.split(",")
            for i in new: # Ranges 1 and 2
                other = i.split("-")
                for x in other: # Loop through each part of the range
                    temp.append(int(x))
            x1, y1, x2, y2 = temp
            if isCompleteRange(x1, y1, x2, y2):
                total += 1

            line = inputObj.readline()

print(total)
