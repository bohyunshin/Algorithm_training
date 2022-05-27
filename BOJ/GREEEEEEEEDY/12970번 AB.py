n,k = map(int,input().split())
ans = ''
for a in range(n):
    b = n-a
    if a*b >= k:
        cnt = [0]*(b+1)
        for i in range(a):
            x = min(b,k)
            cnt[x] += 1
            k -= x
        ans = ''
        for i in range(b,-1,-1):
            for j in range(cnt[i]):
                ans += 'A'
            if i > 0:
                ans += 'B'
        print(ans)
        exit()
print(-1)