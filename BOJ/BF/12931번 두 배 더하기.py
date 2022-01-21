n = int(input())
b = list(map(int,input().split()))
a = [0]*n
MIN = -1
for i in b:
    if MIN == -1 or MIN > i:
        MIN = i
ans = 0
# 먼저 1로 만들기.
ans += n
# 최솟값까지 2 곱하기.
