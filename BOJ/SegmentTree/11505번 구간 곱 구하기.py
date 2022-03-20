from math import log2, ceil
import sys
input = sys.stdin.readline
__div__ = 1000000007

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node] % __div__
    tree[node] = (init(node*2, start, (start+end)//2)) * \
                 (init(node*2 + 1, (start+end)//2 + 1, end))
    return tree[node] % __div__

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        # print(tree[node],node)
        return tree[node] % __div__
    if end < left or right < start:
        return 1
    return ((subsum(node*2, start, (start+end)//2, left, right)) * \
           (subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)))

def update(node, start, end, index, old, new):
    if not (start <= index <= end):
        return
    elif start == end:
        tree[node] = new
        return
    # if start != end:
    #     update(node*2, start, (start+end)//2, index, old, new)
    #     update(node*2 + 1, (start+end)//2 + 1, end, index, old, new)

    update(node * 2, start, (start + end) // 2, index, old, new)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, old, new)

    tree[node] = tree[node*2] * tree[node*2 + 1] % __div__

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
        old = l[b]
        new = c
        l[b] = new
        update(1, 0, n-1, b, old, new)
    if a == 2:
        b -= 1
        c -= 1
        print(subsum(1, 0, n-1, b, c) % __div__)
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