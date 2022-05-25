n,m,k = map(int,input().split())
team = 0
while n >= 2 and m >= 1:
    team += 1
    n -= 2
    m -= 1
s = n+m
if s >= k:
    print(team)
else:
    k -= s
    while k >= 1:
        k -= 3
        team -= 1
    print(team)

"""
10 1 9
1 10 10
"""