from collections import defaultdict, deque
from copy import deepcopy
A=B=C=0
state = {}
circle = ['A','B','C']
for c in circle:
    state[c] = {}
    for i in ['A','B','C']:
        state[c][i] = 0
for k in range(3):
    a = input()
    if a[0] == '0':
        state[circle[k]]['LAST'] = 0
        continue
    cnt,init = a.split()
    for index,i in enumerate(init):
        if i == 'A':
            state[circle[k]]['A'] += 1
        elif i == 'B':
            state[circle[k]]['B'] += 1
        else:
            state[circle[k]]['C'] += 1

        if index == len(init)-1:
            state[circle[k]]['LAST'] = i
def make_key(dct):
    circle = ['A','B','C']
    result = ''
    for c in circle:
        result += c + '/'
        for k in circle:
            result += k + str(dct[c][k])
        if c != 'C':
            result += ','
    return result
# print(state)
state_vis = make_key(state)
visited = defaultdict(int)
visited[state_vis] = 0
q = deque()
q.append(state)

def put_queue(nA,nB,nC,A,B,C):
    global visited, q
    if (nA,nB,nC) not in visited.keys():
        visited[(nA,nB,nC)] = visited[(A,B,C)] + 1
        q.append((nA,nB,nC))

def check(state):
    circle = ['A','B','C']
    for c in circle:
        other_circle = list(set(circle) - set([c]))
        for k in other_circle:
            if state[c][k] >= 1:
                return False
    return True

while q:
    state = q.popleft()
    before_state = make_key(state)
    if check(state):
        print(visited[before_state])
        break
    # A -> B,C
    if state['A']['LAST'] != 0:
        LAST = state['A']['LAST']
        # A -> B
        n_state = deepcopy(state)
        n_state['A'][LAST] -= 1
        n_state['B'][LAST] += 1
        n_state['B']['LAST'] = LAST
        state_vis = make_key(n_state)
        if state_vis not in visited.keys():
            visited[state_vis] = visited[before_state] + 1
            q.append(n_state)
        # A -> C
        n_state = deepcopy(state)
        n_state['A'][LAST] -= 1
        n_state['C'][LAST] += 1
        n_state['C']['LAST'] = LAST
        state_vis = make_key(n_state)
        if state_vis not in visited.keys():
            visited[state_vis] = visited[before_state] + 1
            q.append(n_state)

    # B -> A,C
    if state['A']['LAST'] != 0:
        LAST = state['A']['LAST']
        # A -> B
        n_state = deepcopy(state)
        n_state['A'][LAST] -= 1
        n_state['B'][LAST] += 1
        n_state['B']['LAST'] = LAST
        state_vis = make_key(n_state)
        if state_vis not in visited.keys():
            visited[state_vis] = visited[before_state] + 1
            q.append(n_state)
        # A -> C
        n_state = deepcopy(state)
        n_state['A'][LAST] -= 1
        n_state['C'][LAST] += 1
        n_state['C']['LAST'] = LAST
        state_vis = make_key(n_state)
        if state_vis not in visited.keys():
            visited[state_vis] = visited[before_state] + 1
            q.append(n_state)