from collections import deque
MAX = 10000
check = [False]*(MAX+1)
check[0] = check[1] = True
for i in range(2, MAX+1):
    if check[i] is False:
        j = i*i
        while j <= MAX:
            check[j] = True
            j += i
n = int(input())
for _ in range(n):
    x,y = input().split()
    visited = [-1] * (MAX + 1)
    visited[int(x)] = 0
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == y:
            break
        for i in range(4):
            if i == 0:
                candi = [str(j) for j in range(1,10) if j != x[i]]
            else:
                candi = [str(j) for j in range(10) if j != x[i]]
            for c in candi:
                tmp = [j for j in x]
                tmp[i] = c
                change = ''.join(tmp)
                if visited[int(change)] == -1 and check[int(change)] is False:
                    visited[int(change)] = visited[int(x)] + 1
                    q.append(change)
    print(visited[int(y)] if visited[int(y)] != -1 else 'Impossible')