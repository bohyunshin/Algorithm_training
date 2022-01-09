from itertools import combinations
h,w = map(int,input().split())
n = int(input())
s = []
ans = 0
for _ in range(n):
    r,c = map(int,input().split())
    s.append((r,c))
a = [[0]*w for _ in range(h)]
for c in combinations(s,2):
    (a,b),(x,y) = c
    cases = [((a,b),(x,y)), ((a,b),(y,x)), ((b,a),(x,y)), ((b,a),(y,x))]
    for case in cases:
        (a,b),(x,y) = case
        if a <= h and b <= w and x <= h and y <= w:
            # 정방향
            i,j = h-a,w
            k,l = h,w-b
            if (x <= i and y <= j) or (x <= k and y <= l):
                ans = max(ans, a*b + x*y)
print(ans)