from collections import deque, defaultdict
a,b,c = map(int, input().split())
myhash = {(a,b,c):0}
q = deque()
q.append((a,b,c))

def append_queue(na,nb,nc, a,b,c):
    if (na,nb,nc) not in myhash.keys():
        myhash[(na,nb,nc)] = myhash[(a,b,c)] + 1
        q.append((na,nb,nc))
    else:
        if myhash[(na,nb,nc)] > myhash[(a,b,c)] + 1:
            myhash[(na, nb, nc)] = myhash[(a, b, c)] + 1
            q.append((na, nb, nc))

while q:
    a,b,c = q.popleft()
    # print(a,b,c)
    if a == b and b == c:
        print(1)
        exit()

    if a > b:
        na,nb,nc = a-b, b+b, c
    else:
        na,nb,nc = a+a, b-a, c
    append_queue(na,nb,nc,a,b,c)

    if a > c:
        na,nb,nc = a-c, b, c+c
    else:
        na,nb,nc = a+a, b, c-a
    append_queue(na,nb,nc,a,b,c)

    if b > c:
        na,nb,nc = a, b-c, c+c
    else:
        na,nb,nc = a, b+b, c-b
    append_queue(na,nb,nc,a,b,c)

print(0)
