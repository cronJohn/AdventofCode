temp = []
shouldEscape = False
output_num = 0

def parse(string, start):
    global shouldEscape

    length = 14
    combo_len = len(set(string[start:start+length]))
    if combo_len == length:
        shouldEscape = True
        return start + length
    return 0
        
with open('day6-input.txt','r') as inputObj:
        line = inputObj.readline()

for i in range(0, len(line)):
    output_num = parse(line, i)
    if shouldEscape:
        break

print(f'output_num {output_num}')


