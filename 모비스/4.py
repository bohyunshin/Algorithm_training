from collections import defaultdict
def recursive(l,y,index,ans):
    if set(l) == set(y):
        ans[index] = 1
        return
    if len(l) == len(y) and set(l) != set(y):
        if ans[index] != 1:
            ans[index] = 0
        return
    n = len(l)
    for i in range(n):
        for j in range(i+1,n):
            add = l[i] + l[j]
            tmp = [k for index,k in enumerate(l) if index not in [i,j]]
            tmp.append(add)
            recursive(tmp,y,index,ans)

def solution(p, q):
    ans = defaultdict(int)
    for index,(x,y) in enumerate(zip(p,q)):
        recursive(x,y,int(index),ans)
    return [True if ans[i] == 1 else False for i in range(len(p))]