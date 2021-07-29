n,m = map(int, input().split())
a = sorted(list(map(int, input().split())))

answer = [0]*m
v = [False]*10001

def solution(index,a,n,m):
    if index == m:
        print(' '.join(list(map(str,answer))))
        return
    for ii,i in enumerate(a):
        if v[i]:
            continue
        v[i] = True
        answer[index] = i
        solution(index+1,[l for k,l in enumerate(a) if k > ii],n,m)
        v[i] = False
solution(0,a,n,m)