from collections import deque
a,b,c,d = map(int,input().split())

def add_to_queue(nx,ny,x,y):
    if visited.get((nx,ny)) == None:
        q.append((nx,ny))
        visited[(nx,ny)] = visited[(x,y)]+1
# def fill(x,limit):
#     if x < limit:
#         limit
def move(from_,to_,which):
    limit = b if which == 'a' else a
    if from_ <= limit - to_:
        return (0,to_ + from_)
    else:
        return (from_ - (limit - to_), to_ + (limit - to_))

# print(move(2,2,'b'))

q = deque()
visited = {}
q.append((0,0))
visited[(0,0)] = 0
while q:
    x,y = q.popleft()
    if (x,y) == (c,d):
        print(visited[(x,y)])
        exit()
        break
    # F(x)
    if x < a:
        add_to_queue(a,y,x,y)
    # F(y)
    if y < b:
        add_to_queue(x,b,x,y)
    # E(x)
    if x > 0:
        add_to_queue(0,y,x,y)
    # E(y)
    if y > 0:
        add_to_queue(x,0,x,y)
    # M(x,y)
    nx,ny = move(x,y,'a')
    add_to_queue(nx,ny,x,y)
    # M(y,x)
    ny,nx = move(y,x,'b')
    add_to_queue(nx,ny,x,y)
print(-1)