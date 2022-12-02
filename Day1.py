currentElf = 0
calorieArray = []
currentCounter = 0

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


