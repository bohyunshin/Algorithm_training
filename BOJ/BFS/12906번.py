from collections import defaultdict, deque
from copy import deepcopy
A=B=C=0
state = []
for k in range(3):
    a = input()
    if a[0] == '0':
        state.append([])
        continue
    cnt,init = a.split()
    state.append([i for i in init])
def make_key(state):
    result = ''
    for i in state:
        result += ''.join(i)
        result += '/'
    return result[:-1]

state_vis = make_key(state)
visited = defaultdict(int)
visited[state_vis] = 0
q = deque()
q.append(state)

def check(state):
    circle = ['A','B','C']
    for index,i in enumerate(state):
        other_circle = set(circle) - set([circle[index]])
        if len(set(i) & other_circle) >= 1:
            return False
    return True

while q:
    state = q.popleft()
    state_vis = make_key(state)
    if check(state):
        print(visited[state_vis])
        break
    # A -> B,C
    if len(state[0]) >= 1:
        # A -> B
        n_state = deepcopy(state)
        LAST = n_state[0][-1]
        n_state[0] = n_state[0][:-1]
        n_state[1].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)
        # A -> C
        n_state = deepcopy(state)
        LAST = n_state[0][-1]
        n_state[0] = n_state[0][:-1]
        n_state[2].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)

    # B -> A,C
    if len(state[1]) >= 1:
        # B -> A
        n_state = deepcopy(state)
        LAST = n_state[1][-1]
        n_state[1] = n_state[1][:-1]
        n_state[0].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)
        # B -> C
        n_state = deepcopy(state)
        LAST = n_state[1][-1]
        n_state[1] = n_state[1][:-1]
        n_state[2].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)

    # C -> A,B
    if len(state[2]) >= 1:
        # C -> A
        n_state = deepcopy(state)
        LAST = n_state[2][-1]
        n_state[2] = n_state[2][:-1]
        n_state[0].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)
        # C -> B
        n_state = deepcopy(state)
        LAST = n_state[2][-1]
        n_state[2] = n_state[2][:-1]
        n_state[1].append(LAST)
        n_state_vis = make_key(n_state)
        if n_state_vis not in visited.keys():
            visited[n_state_vis] = visited[state_vis] + 1
            q.append(n_state)