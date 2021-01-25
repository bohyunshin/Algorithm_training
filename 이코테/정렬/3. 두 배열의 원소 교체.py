n,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A, B를 정렬
A.sort()
B.sort(reverse=True)

A_index = 0
B_index = 0
for i in range(k):
    if A_index >= n or B_index >= n:
        continue
    else:
        if A[A_index] < B[B_index]:
            A[A_index], B[B_index] = B[B_index], A[A_index]
            A_index += 1
            B_index += 1
        else:
            B_index += 1

print(sum(A))
