threshold = 100000

# Code help from https://www.youtube.com/watch?v=XvA0iO_gvfM
cwd = root = {}
stack = []

def parse(string):
    global cwd
    global stack

    if string[0] == "$":
        if string[2] == "c":
            dir = string[5:]
            if dir == "/":
                cwd = root
                stack = []
            elif dir == "..":
                cwd = stack.pop()
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]
    else:
        x, y = string.split()
        if x == "dir":
            if y not in cwd:
                cwd[y] = {}
        else:
            cwd[y] = int(x)

temp = []
def loop(dir = root):
    global temp
    if type(dir) == int:
        return (dir, 0)

    size = 0
    ans = 0

    for el in dir.values():
        s, a = loop(el)
        size += s
        ans += a

    if size <= threshold:
        ans += size

    temp.append(size)
    return (size, ans)

with open('day7-input.txt','r') as inputObj:
    line = inputObj.readline().strip()

    while line:
        parse(line)
        line = inputObj.readline().strip()

loop()
total_size = 70000000
target_unused_size = 30000000

temp.sort(reverse=True)

other = []
for num in temp:
    unused = total_size - temp[0]
    if (num + unused) >= target_unused_size:
        other.append(num)

print(f'answer: {min(other)}') 
