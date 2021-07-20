n,m = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
S = A[0]
answer = 0

# two pointer
# 시간 복잡도는 O(n)
while left <= right and right < n:
    if S < m:
        right += 1
        if right < n:
            S += A[right]
    elif S == m:
        answer += 1
        right += 1
        if right < n:
            S += A[right]
    elif S > m:
        S -= A[left]
        left += 1
        if left > right and left < n:
            right = left
            S = A[left]
print(answer)