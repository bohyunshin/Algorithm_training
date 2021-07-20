n = int(input())
check = [False] * (n+1)
A = []
for i in range(2, n+1):
    if check[i]:
        continue
    j = i*2
    A.append(i)
    while j <= n:
        check[j] = True
        j += i

left = 0
right = 0
s = A[0]
answer = 0

while left <= right and right < len(A):
    if s < n:
        right += 1
        if right < len(A):
            s += A[right]
    elif s == n:
        answer += 1
        right += 1
        if right < len(A):
            s += A[right]
    elif s > n:
        s -= A[left]
        left += 1
        if left > right and left < len(A):
            right = left
            s = A[left]
print(answer)