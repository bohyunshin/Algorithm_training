n = int(input())
# check: 소수가 아닌 애들을 True로 담아둠.
# A: 소수를 담아둠.
check = [False] * (n+1)
A = []
for i in range(2, n+1):
    if check[i]:
        continue
    # check[i]가 False면 소수라는 뜻이니까 A에 추가해주고,
    # j는 소수 i의 배수로 check에 확인했다고 표시해줌.
    j = i*2
    A.append(i)
    while j <= n:
        check[j] = True
        j += i

left = 0
right = 0
s = A[0]
answer = 0
# 그 이후로는 two pointer
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