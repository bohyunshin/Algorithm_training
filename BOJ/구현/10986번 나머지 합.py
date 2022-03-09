from collections import defaultdict
n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
s = [0]*(n+1)
dct = defaultdict(int)
ans = 0
for i in range(1,n+1):
    s[i] = (s[i-1]%m + a[i]%m) % m
    if s[i] % m == 0:
        ans += 1
    dct[s[i]] += 1
for mod in dct.keys():
    v = dct[mod]
    ans += v*(v-1)/2
print(int(ans))