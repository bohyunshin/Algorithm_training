from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    q = deque()
    dist = [-1]*n
    how = [-1]*n
    via = [-1]*n
    # 초기값 설정: 1로 스타트
    dist[1%n] = 0
    how[1%n] = 1
    q.append(1%n)
    while q:
        now = q.popleft()
        for i in [0,1]:
            next_ = (now*10 + i)%n
            if dist[next_] == -1:
                dist[next_] = dist[now]+1
                how[next_] = i
                via[next_] = now
                q.append(next_)
    if dist[0] == -1:
        print("BRAK")
    else:
        ans = ''
        i = 0
        while i != -1:
            ans += str(how[i])
            i = via[i]
        print(ans[::-1])