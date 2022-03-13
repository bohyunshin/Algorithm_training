from collections import defaultdict, deque
n,m = map(int,input().split())
possible = defaultdict(list)
for _ in range(m):
    x,y,a,b = map(int,input().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1
    possible[(x,y)].append((a,b))
def to_number(x,y):
    return x*n + y
def make_key(lst):
    ans = []
    for x,y in lst:
        ans.append(to_number(x,y))
    ans.sort()
    return ' '.join(map(str,ans))
def make_turn_on(key):
    ans = []
    for number in key.split(' '):
        x,y = int(number) // n, int(number) % n
        ans.append((x,y))
    return ans
q = deque()
visited = {}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
turn_on = [(0,0)]
for x,y in possible[(0,0)]:
    turn_on.append((x,y))
key = make_key(turn_on)
visited[(0,0,key)] = 0
q.append((0,0,key))
ans = len(turn_on)
while q:
    x,y,key = q.popleft()
    turn_on = make_turn_on(key)
    # print(x,y,turn_on)
    # print(ans)
    if ans < len(turn_on):
        ans = len(turn_on)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # turn_on_new = turn_on[:]
            turn_on_new = set(turn_on)
            for w,z in possible[(nx,ny)]:
                # if (w,z) not in turn_on_new:
                #     turn_on_new.append((w,z))
                turn_on_new.add((w,z))
            if (nx,ny) not in turn_on_new:
                continue
            key_new = make_key(turn_on_new)
            if visited.get((nx,ny,key_new)) == None:
                visited[(nx,ny,key_new)] = visited[(x,y,key)] + 1
                q.append((nx,ny,key_new))
print(ans)

"""
3 1
3 3 2 2
"""