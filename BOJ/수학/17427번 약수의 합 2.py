n = int(input())
answer = 0
d = 1
while True:
    if d > n:
        break
    answer += (n // d) * d
    d += 1
print(answer)
