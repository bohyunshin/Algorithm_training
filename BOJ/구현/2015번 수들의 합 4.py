from collections import defaultdict
n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
s = [0]*(n+1)
ans = 0
stl = defaultdict(int)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
    if s[i] == k:
        ans += 1
    ans += stl[s[i] - k]
    stl[s[i]] += 1
print(ans)