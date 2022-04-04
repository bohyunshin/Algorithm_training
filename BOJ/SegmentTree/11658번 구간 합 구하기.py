from math import log2, ceil
import sys
input = sys.stdin.readline

def xinit(node, start, end):
    return

def yinit(node, start, end, x1, x2):
    if start == end:
        return xinit(1, x1, x2)
    tree

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

def update(x1,y1,d):
    i,j = y1,x1
    tree[i][j] = d
    while j > 0:
        j = j // 2
        tree[i][j] = tree[i][j*2] + tree[i][j*2 + 1]
    while i > 0:
        j = x1
        i = i // 2
        tree[i][j] = tree[i*2][j] + tree[i*2 + 1][j]
        while j > 0:
            j = j // 2
            tree[i][j] = tree[i][j*2] + tree[i][j*2 + 1]

n,m = map(int,input().split())
h = int(ceil(log2(n)))
tree = [[0]*(2**(h+1)) for _ in range(2**(h+1))]
l = []
for i in range(n):
    cur = list(map(int,input().split()))
    for j in range(n):
        update(i,j,cur[j])
for k in range(len(tree)):
    print(tree[k])

# init(1, 0, n-1)

# for _ in range(m+k):
#     a,b,c = map(int,input().split())
#     if a == 1:
#         b -= 1
#         diff = c-l[b]
#         l[b] = c
#         update(1, 0, n-1, b, diff)
#     if a == 2:
#         b -= 1
#         c -= 1
#         print(subsum(1, 0, n-1, b, c))
