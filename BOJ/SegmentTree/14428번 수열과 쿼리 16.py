from math import log2, ceil
import sys
input = sys.stdin.readline

def get_idx(val_l,val_r,idx_l,idx_r):
    if val_l < val_r:
        return idx_l
    elif val_l > val_r:
        return idx_r
    else:
        return min(idx_l,idx_r)

def init(node, start, end):
    if start == end:
        tree[node] = l[start],start
        return tree[node]
    val_l, idx_l = init(node*2, start, (start+end)//2)
    val_r, idx_r = init(node*2 + 1, (start+end)//2 + 1, end)
    idx = get_idx(val_l,val_r,idx_l,idx_r)
    tree[node] = l[idx],idx
    return tree[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return (1e100,1e100)
    val_l, idx_l = subsum(node*2, start, (start+end)//2, left, right)
    val_r, idx_r = subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)
    idx = get_idx(val_l,val_r,idx_l,idx_r)
    return (l[idx], idx)

def update(node, start, end, index, new):
    if not (start <= index <= end):
        return
    elif start == end:
        val_old, idx_old = tree[node]
        val_new, idx_new = new, index
        idx = get_idx(val_old,val_new,idx_old,idx_new)
        if idx == idx_new:
            tree[node] = (val_new, idx_new)
        return
    # if start != end:
    update(node*2, start, (start+end)//2, index, new)
    update(node*2 + 1, (start+end)//2 + 1, end, index, new)

    val_l, idx_l = tree[node*2]
    val_r, idx_r = tree[node*2 + 1]
    idx = get_idx(val_l, val_r, idx_l, idx_r)
    tree[node] = l[idx], idx

n = int(input())
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
l = list(int(i) for i in input().split())
m = int(input())
init(1, 0, n-1)

for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 1:
        b -= 1
        l[b] = c
        update(1, 0, n-1, b, c)
    if a == 2:
        b -= 1
        c -= 1
        print(subsum(1, 0, n-1, b, c)[1]+1)
"""
8
0
1
2
3
4
5
6
7
"""