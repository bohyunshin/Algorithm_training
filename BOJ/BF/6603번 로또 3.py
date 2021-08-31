def go(a,c,S,index,start,k,m):
    if index >= m:
        print(' '.join(list(map(str,a))))
        return
    for i in range(start,k):
        if c[i]:
            continue
        c[i] = True
        a[index] = S[i]
        go(a,c,S,index+1,i+1,k,m)
        c[i] = False
    # return a

def solution(A):
    k, S = A[0], A[1:]
    S.sort()
    m = 6
    a = [0] * m
    c = [False] * k
    go(a,c,S,0,0,k,m)


if __name__ == '__main__':
    while True:
        A = list(map(int, input().split()))
        if A[0] == 0:
            break
        solution(A)
        print()