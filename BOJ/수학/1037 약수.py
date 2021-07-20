num = int(input())
A = list(map(int,input().split()))
A.sort()
if len(A) % 2 == 1:
    mid = int((len(A)-1)/2)
    print(A[mid]**2)
else:
    mid = int(len(A)/2)
    print(A[mid-1]*A[mid])