from math import log2, ceil
import sys
input = sys.stdin.readline

def subsum(node, start, end, k):
    if start == end:
        print(start+1)
        return start
    if node*2 <= tree_size-1 and tree[node*2] >= k:
        return subsum(node*2, start, (start+end)//2, k)
    k -= tree[node*2]
    if node*2 + 1 <= tree_size-1 and tree[node*2 + 1] >= k:
        return subsum(node*2 + 1, (start+end)//2 + 1, end, k)

def update(node, start, end, index, diff):
    if not (start <= index <= end):
        return
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)

MAX = 1000000
n = int(input())
h = int(ceil(log2(MAX)))
tree = [0]*(2**(h+1))
tree_size = len(tree)
l = [0]*(MAX)

# init(1, 0, n-1)

for _ in range(n):
    cur = list(map(int,input().split()))
    ret = 0
    if cur[0] == 1:
        _, b = cur
        idx = subsum(1,0,MAX-1,b)
        l[idx] -= 1
        update(1,0,MAX-1,idx,-1)
    if cur[0] == 2:
        _, b, c = cur
        update(1,0,MAX-1,b-1,c)

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