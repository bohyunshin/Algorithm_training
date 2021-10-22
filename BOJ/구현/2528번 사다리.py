n,l = map(int,input().split())
sticks = []
direction = []
for _ in range(n):
    length,d = map(int,input().split())
    sticks.append(length)
    direction.append(d)
# d == 0 왼->오
# d == 1 오->왼
location = {}
for i,length in enumerate(sticks):
    if direction[i] == 0:
        location[i] = [0,length]
    else:
        location[i] = [l-length,l]
time = 0
step = 0
dx = [1,-1]
# 맨 윗층에 올라갈때 까지 반복 수행.
while step != n-1:
    while step < n-1:
        if location[step+1][1] < location[step][0] or \
            location[step+1][0] > location[step][1]:
            break
        else:
            step += 1
    if step == n-1:
        break
    # 막대기 이동시키기.
    for i in range(n):
        start,end = location[i]
        if end-start == l:
            continue
        # 막대기가 현재 젤 왼쪽에 있으면, 방향 업데이트해주고 이동시켜줌.
        if start == 0:
            direction[i] = 0
            location[i] = [start+1,end+1]
        # 막대기가 현재 젤 오른쪽에 있으면, 방향 업데이트해주고 이동시켜줌.
        elif end == l:
            direction[i] = 1
            location[i] = [start-1,end-1]
        # 남은 경우는, 방향에 따라서 막대기 이동시켜 줌.
        else:
            d = direction[i]
            location[i] = [start+dx[d],end+dx[d]]
    time += 1
print(time)

"""
2 12
6 0
6 1
"""