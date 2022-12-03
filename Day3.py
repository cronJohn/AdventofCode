def getHalf(string):
    return int(len(string)/2)

total = 0
group = 0

ratings = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
}

temp = []

with open('day3-input.txt','r') as inputObj:
        line = inputObj.readline()

        while line:
            word = str(line.strip())
            temp.append(word)
            group += 1

            #totalhalf = getHalf(word)

            #first = word[:totalhalf]
            #second = word[totalhalf:]

            line = inputObj.readline()
            
            if (group % 3 == 0) and (group != 0):
                union = set(temp[0]).intersection(temp[1], temp[2])
                for i in union:
                    if i.isupper():
                        total += ratings[i.lower()] + 26
                    else:
                        total += ratings[i.lower()]
                temp = []
                group = 0
                union = []
print(total)
