# 내 풀이
n, m = map(int, input().split())
rowise_min = []
for i in range(n):
    one_row = list(map(int, input().split()))
    rowise_min.append(min(one_row))
print(max(rowise_min))

