def go(a,c,A,index,start,m,S):
    if index >= m:
        if sum(a) == S:
            return 1
        return 0
    n = len(A)
    cnt = 0
    for i in range(start,n):
        if c[i]:
            continue
        c[i] = True
        a[index] = A[i]
        cnt += go(a,c,A,index+1,i+1,m,S)
        c[i] = False
    return cnt

def solution(n,S,A):
    ans = 0
    for m in range(1,n+1):
        a = [0]*m
        c = [False]*n
        ans += go(a,c,A,0,0,m,S)
    return ans

if __name__ == '__main__':
    n,s = map(int, input().split())
    A = list(map(int, input().split()))
    ans = solution(n,s,A)
    print(ans)