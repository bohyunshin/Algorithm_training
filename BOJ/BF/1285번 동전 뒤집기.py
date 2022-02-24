from copy import deepcopy
from collections import deque
n = int(input())
coin = []
for _ in range(n):
    coin.append(list(i for i in input()))
def make_key(coin):
    key = ''
    for i in range(n):
        key += ''.join(coin[i]) + ' '
    return key.strip()
def make_coin(key):
    coin = []
    for i in key.split(' '):
        coin.append(list(k for k in i))
    return coin
def append_queue(key_now, key_before):
    if visited.get(key_now) == None:
        q.append(key_now)
        visited[key_now] = visited[key_before] + 1
def twist(c):
    return 'H' if c == 'T' else 'T'
key = make_key(coin)
q = deque()
visited = {}
q.append(key)
visited[key] = 0
ans = 0
while q:
    key_before = q.popleft()
    print(key_before)
    coin = make_coin(key_before)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if coin[i][j] == 'T':
                cnt += 1
    if ans == 0 or ans > cnt:
        ans = cnt
    for i in range(n):
        coin_copy = deepcopy(coin)
        # 행 바꾸기.
        for k in range(n):
            coin_copy[i][k] = twist(coin_copy[i][k])
        key_now = make_key(coin_copy)
        append_queue(key_now, key_before)
        # 행 원래대로.
        for k in range(n):
            coin_copy[i][k] = twist(coin_copy[i][k])

        # 열 바꾸기.
        for k in range(n):
            coin_copy[k][i] = twist(coin_copy[k][i])
        key_now = make_key(coin_copy)
        append_queue(key_now, key_before)
        # 행 원래대로.
        for k in range(n):
            coin_copy[k][i] = twist(coin_copy[k][i])
print(ans)

"""
3
TTT
TTT
TTT

20
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
"""