total = 0

def isCompleteRange(x1, y1, x2, y2):
    range1 = range(x1, y1)
    range2 = range(x2, y2)
    
    # Everyone uses Stack Overflow
    # Source: https://stackoverflow.com/questions/32480423/how-to-check-if-a-range-is-a-part-of-another-range-in-python-3-x
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

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
                print(f'the temp array {temp}')
                print("true")
                total += 1
            else:
                if isCompleteRange(x1, y1, x2, y2):
                    print(f'the temp array {temp}')
                    print("else true")
                    total += 1
                else:
                    print(f'the temp array {temp}')
                    print('not')

            line = inputObj.readline()

print(total)
