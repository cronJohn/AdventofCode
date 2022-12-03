# Rock-1 Paper-2 Scissor-3
# Lose-0 Draw-3 Win-6
# X-Lose Y-Draw Z-Win

scoresdict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "A": 1,
        "B": 2,
        "C": 3,
}

total = 0

def getwinningscorepart1(opp, player):
    if (opp == "A" and player == "X") or (opp == "B" and player == "Y") or (opp == "C" and player == "Z"): # Tie
        return scoresdict[player] + 3
    elif (opp == "A" and player == "Z") or (opp == "B" and player == "X") or (opp == "C" and player == "Y"): # Lose
        return scoresdict[player]
    else:
        return scoresdict[player] + 6

def getwinningscorepart2(opp, ending):
    if ending == "X": # Lose
        if opp == "A":
            return 3
        elif opp == "B":
            return 1
        else:
            return 2

    elif ending == "Y": # Draw
        return scoresdict[opp] + 3

    else: # Win
        if opp == "A":
            return 8 
        elif opp == "B":
            return 9
        else:
            return 7

with open('day2-input.txt','r') as inputObj:
        line = inputObj.readline()

        while line:
            word = line.strip() 
            first = word[0]
            second = word[-1]

            #total += getwinningscore(first, second)
            total += getwinningscorepart2(first, second)

            line = inputObj.readline()
print(total)

