from math import log2, ceil

def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]
    tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2+1, end)
    return tree[node]
def query(node, start, end, val):
    if start == end:
        return start
    if val < tree[node*2 + 1]:
        return query(node*2 + 1, (start+end)//2 + 1, end, val)
    else:
        return query(node * 2, start, (start + end) // 2, val - tree[node * 2 + 1])
def update(node, start, end, index):
    if not (start <= index <= end):
        return
    tree[node] -= 1
    if start != end:
        update(node*2, start, (start+end)//2, index)
        update(node*2 + 1, (start+end)//2 + 1, end, index)

n = int(input())
l = list(map(int,input().split()))
# h = int(ceil(log2(n)))
# tree = [0]*(2**(h+1))
tree = [0]*(4*n)
ans = [0]*n
init(1,0,n-1)
for i in range(n-1,-1,-1):
    idx = query(1,0,n-1,l[i])
    ans[idx] = i+1
    update(1,0,n-1,idx)
for i in ans:
    print(i, end=' ')