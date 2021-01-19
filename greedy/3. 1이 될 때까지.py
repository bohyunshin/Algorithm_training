# 내 풀이
n, k = map(int, input().split())

execution = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    execution += 1
print(n, execution)