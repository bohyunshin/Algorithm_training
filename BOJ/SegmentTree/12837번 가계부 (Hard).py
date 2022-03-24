from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2 + 1, end)
    return tree[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return 0
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)

def update(node, start, end, index, diff):
    if not (start <= index <= end):
        return
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)

n,q = map(int,input().split())
l = [0]*n
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
init(1, 0, n-1)
for _ in range(q):
    cur = list(map(int,input().split()))
    if cur[0] == 1:
        _,p,new = cur
        p -= 1
        # diff = new-l[p]
        l[p] += new
        update(1,0,n-1,p,new)
    else:
        _,p,q = cur
        p -= 1
        q -= 1
        print(subsum(1,0,n-1,p,q))

"""
10 8
1 3 10000
1 4 -5000
1 7 -3000
2 1 10
1 6 35000
2 4 10
1 4 5000
2 4 10
"""