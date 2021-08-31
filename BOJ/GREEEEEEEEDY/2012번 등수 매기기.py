n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
A.sort()
ans = 0
for i in range(n):
    ans += abs(i+1-A[i])
print(ans)