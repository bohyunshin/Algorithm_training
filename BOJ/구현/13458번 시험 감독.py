n = int(input())
A = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0
# 총 감독관.
for i in range(n):
    cnt += 1
    A[i] -= b
# 부 감독관.
for i in range(n):
    if A[i] > 0:
        div,mod = A[i] // c, A[i] % c
        cnt += div
        if mod >= 1:
            cnt += 1
print(cnt)