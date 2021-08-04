n = 8
A = [0]*8

def merge(a,m,middle,n):
    i = m
    j = middle + 1
    k = m
    while i <= middle and j <= n:
        if a[i] <= a[j]:
            A[k] = a[i]
            i += 1
        else:
            A[k] = a[j]
            j += 1
        k += 1
    # i가 먼저 끝나거나 j가 먼저 끝났을 때 남은 애들도 다 넣어줘야 함.
    # i가 먼저 끝났을 때.
    if i > middle:
        # 남은 j값을 모두 넣어준다.
        for t in range(j,n+1):
            A[k] = a[t]
            k += 1
    # j가 먼저 끝났을 때
    else:
        for t in range(i,middle+1):
            A[k] = a[t]
            k += 1
    # 정열된 배열을 삽입
    for t in range(m,n+1):
        a[t] = A[t]

def mergeSort(a, m, n):
    # 크기가 1보다 큰 경우
    if m < n:
        middle = (m+n) // 2
        # MERGE
        # 왼쪽 병합 정렬
        mergeSort(a,m,middle)
        # 오른쪽 병합 정렬
        mergeSort(a, middle+1,n)

        # SORT
        merge(a,m,middle,n)

array = [7,6,5,8,3,5,9,1]
mergeSort(array, 0, len(array)-1)
print(array)