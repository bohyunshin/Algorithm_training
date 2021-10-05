from copy import deepcopy
T = []
for _ in range(4):
    T.append([int(i) for i in input()])
k = int(input())
rotate = []
for _ in range(k):
    a,b = map(int,input().split())
    a -= 1
    rotate.append((a,b))

def rotate_clockwise(l):
    result = []
    result.append(l[-1])
    for i in l[:-1]:
        result.append(i)
    return result

def rotate_unclockwise(l):
    result = []
    for i in l[1:]:
        result.append(i)
    result.append(l[0])
    return result

def check_identical(T):
    result = []
    for i in range(3):
        if T[i][2] == T[i+1][6]:
            result.append(1)
        else:
            result.append(0)
    return result

for t,d in rotate:
    state = check_identical(T)
    direction = [0]*4
    direction[t] = d
    if t == 0:
        if state[0] == 0:
            direction[1] = -d
            if state[1] == 0:
                direction[2] = d
                if state[2] == 0:
                    direction[3] = -d
    elif t == 1:
        if state[0] == 0:
            direction[0] = -d
        if state[1] == 0:
            direction[2] = -d
            if state[2] == 0:
                direction[3] = d
    elif t == 2:
        if state[2] == 0:
            direction[3] = -d
        if state[1] == 0:
            direction[1] = -d
            if state[0] == 0:
                direction[0] = d
    elif t == 3:
        if state[2] == 0:
            direction[2] = -d
            if state[1] == 0:
                direction[1] = d
                if state[0] == 0:
                    direction[0] = -d
    T_cp = []
    for t,d in enumerate(direction):
        if d == 0:
            T_cp.append(T[t])
        if d == 1:
            T_cp.append(rotate_clockwise(T[t]))
        if d == -1:
            T_cp.append(rotate_unclockwise(T[t]))
    T = deepcopy(T_cp)
score = 0
for i,t in enumerate(T):
    if i == 0 and t[0] == 1:
        score += 1
    if i == 1 and t[0] == 1:
        score += 2
    if i == 2 and t[0] == 1:
        score += 4
    if i == 3 and t[0] == 1:
        score += 8
print(score)