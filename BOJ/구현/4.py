from collections import defaultdict
ans = defaultdict(int)
def recursive(l,y,index):
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
            recursive(tmp,y,index)
recursive([5,3,2,2,1],[7,2,4],0)
recursive([4,3,3],[5,5],1)
print(ans)