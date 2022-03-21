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
    propagate(node, start, end)
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return 0
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)

def update(node, start, end, left, right, diff):
    propagate(node, start, end)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2 + 1] += diff
        return
    update(node*2, start, (start+end)//2, left, right, diff)
    update(node*2 + 1, (start+end)//2 + 1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2 + 1]

def propagate(node, start, end):
    if lazy[node]:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0

n,m,k = map(int,input().split())
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
lazy = [0]*(2**(h+1))
l = []
for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m+k):
    cur = list(int(i) for i in input().split())
    if cur[0] == 1:
        a,b,c,d = cur
        update(1, 0, n-1, b-1, c-1, d)
        # print(tree, d)
    if cur[0] == 2:
        a,b,c = cur
        print(subsum(1, 0, n-1, b-1, c-1))
        # print(tree)
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