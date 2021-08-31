n = int(input())
k = int(input())
A = list(map(int, input().split()))
if n <= k:
    print(0)
else:
    A.sort()
    diff = []
    for i in range(len(A)-1):
        diff.append(A[i+1]-A[i])
    diff.sort()
    print(sum(diff[:n-k]))
# 참조 사이트: https://steady-coding.tistory.com/12