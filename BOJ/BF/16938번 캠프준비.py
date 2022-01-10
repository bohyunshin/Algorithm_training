from itertools import combinations
n,l,r,x = map(int,input().split())
a = list(map(int,input().split()))
# ans = 0
# for k in range(2,n+1):
#     for c in combinations(a,k):
#         if l <= sum(c) <= r and max(c)-min(c) >= x:
#             ans += 1
# print(ans)

c = [False]*(n+1)
def go(index):
    if index == n:
        cnt = 0
        total = 0
        hard = -1
        easy = -1
        for i in range(n):
            if c[i] == False:
                continue
            total += a[i]
            cnt += 1
            if hard == -1 or hard < a[i]:
                hard = a[i]
            if easy == -1 or easy > a[i]:
                easy = a[i]
        if cnt >= 2 and l <= total <= r and hard-easy >= x:
            return 1
        else:
            return 0
    c[index] = True
    cnt1 = go(index+1)
    c[index] = False
    cnt2 = go(index+1)
    return cnt1+cnt2
print(go(0))