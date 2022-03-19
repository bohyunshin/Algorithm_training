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

n,m,k = map(int,input().split())
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
l = []
for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        b -= 1
        diff = c-l[b]
        l[b] = c
        update(1, 0, n-1, b, diff)
    if a == 2:
        b -= 1
        c -= 1
        print(subsum(1, 0, n-1, b, c))
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