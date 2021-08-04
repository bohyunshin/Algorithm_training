n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
answer = 1e100
for i in range(1,2**n - 1):
    a = 0
    b = 0
    start = []
    link = []
    temp = 0
    for k in range(n):
        if i & (1 << k) > 0:
            temp += 1
            start.append(k)
        else:
            link.append(k)
    if temp != n // 2:
        continue

    for j in range(len(start)):
        for l in range(len(start)):
            a += s[start[j]][start[l]]
            b += s[link[j]][link[l]]
    if abs(a-b) < answer:
        answer = abs(a-b)
print(answer)

