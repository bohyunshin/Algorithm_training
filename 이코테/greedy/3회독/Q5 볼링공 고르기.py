n,m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0
for i in range(len(balls)-1):
    counterpart = balls[i+1:]
    for ball in counterpart:
        if balls[i] != ball:
            result += 1
print(result)