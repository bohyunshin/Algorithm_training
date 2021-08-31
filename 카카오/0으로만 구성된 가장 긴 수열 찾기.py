n,m = map(int, input().split())
A = list(map(int, input().split()))


def find_longest_continuous_zero(A):
    m = 0
    left = 0
    right = 0
    S = A[0]
    answer = 0
    MAX_LEN = -1
    n = len(A)

    # two pointer
    # 시간 복잡도는 O(n)
    while left <= right and right < n:
        if S < m:
            right += 1
            if right < n:
                S += A[right]
        elif S == m:
            MAX_LEN = max(MAX_LEN, right-(left-1))
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
    return MAX_LEN
print(find_longest_continuous_zero(A))