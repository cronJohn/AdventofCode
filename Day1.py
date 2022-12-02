currentElf = 0
calorieArray = []
currentCounter = 0

def top3(arr):
    sortedarray = sorted(arr,reverse=True)
    top1 = sortedarray[0]
    top2 = sortedarray[1]
    top3 = sortedarray[2]
    return (top1 + top2 + top3)

# Open puzzle input file
with open('input.txt','r') as inputObj:
        line = inputObj.readline()

        while line:
            if len(line.strip()) == 0: # If there is an empty line
                calorieArray.append(currentCounter)
                currentCounter = 0

            else:
                currentCounter += int(line.strip())

            line = inputObj.readline()
            currentElf += 1

        maxCalories = max(calorieArray)
        print(f'Max calories: {maxCalories}')

        top3total = top3(calorieArray)
        print(f'Top 3 total: {top3total}')



