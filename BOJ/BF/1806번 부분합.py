n,s = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
sum_ = A[0]
answer = 1e100

while left <= right and right < n:
    if sum_ < s:
        right += 1
        if right < n:
            sum_ += A[right]
    if sum_ == s:
        if right - left < answer:
            answer = right - left
        right += 1
        if right < n:
            sum_ += A[right]
    if sum_ > s:
        if right - left < answer:
            answer = right - left
        sum_ -= A[left]
        left += 1
        if left > right and left < n:
            right = left
            sum_ = A[left]
if answer == 1e100:
    print(0)
else:
    print(answer+1)