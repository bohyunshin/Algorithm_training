n = int(input())
check = [False]*(n*50+1)
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            l = n-i-j-k
            val = i+5*j+10*k+50*l
            check[val] = True
ans = 0
for i in range(1,n*50+1):
    if check[i]:
        ans += 1
print(ans)
