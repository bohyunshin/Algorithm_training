lst = [[0,1],[1,2],[3,4]]
a = [0]*3
def recursive(index,m):
    if index >= m:
        print(' '.join(list(map(str, a))))
        return
    A = lst[index]
    for i in range(len(A)):
        a[index] = A[i]
        recursive(index+1,3)
recursive(0,3)