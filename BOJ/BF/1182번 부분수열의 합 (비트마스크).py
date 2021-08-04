n,s = map(int, input().split())
A = list(map(int, input().split()))
m = 2**n-1
answer = 0
for i in range(1,m+1):
    temp = 0
    for k in range(n):
        if i & (1 << k) != 0:
            temp += A[k]
    if temp == s:
        answer += 1
print(answer)