n,x = map(int, input().split())
burger = 'P'
d = [0]*(n+1)
p = [0]*(n+1)
d[0] = 1
p[0] = 1
for i in range(1,n+1):
    d[i] = 2*d[i-1]+3
    p[i] = 2*p[i-1]+1

# n단계에서, 밑에서부터 x개를 먹었을 때 패티의 수.
def go(n,x):
    if n == 0:
        if x == 0:
            return 0
        if x == 1:
            return 1
    if x == 1:
        return 0

    if 1 < x <= 1+d[n-1]:
        return go(n-1,x-1)

    if x == 1 + d[n-1] + 1:
        return p[n-1] + 1

    if 1 + d[n-1] + 1 < x <= 1 + d[n-1] + 1 + d[n-1]:
        return p[n-1] + 1 + go(n-1, x-(1+d[n-1]+1))

    if x == 1 + d[n-1] + 1 + d[n-1] + 1:
        return p[n-1] + 1 + p[n-1]
print(go(n,x))