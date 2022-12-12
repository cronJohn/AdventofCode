with open('day11-input.txt','r') as inputObj:
        line = inputObj.read().strip()
        parts = line.split("\n\n")

for i, part in enumerate(parts):
    lines = part.split("\n")
    print(lines)
