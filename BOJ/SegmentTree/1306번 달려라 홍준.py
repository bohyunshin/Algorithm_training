from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    tree[node] = max(init(node*2, start, (start+end)//2),init(node*2 + 1, (start+end)//2 + 1, end))
    return tree[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return -1
    return max(subsum(node*2, start, (start+end)//2, left, right),subsum(node*2 + 1, (start+end)//2 + 1, end, left, right))

# def update(node, start, end, index, diff):
#     if not (start <= index <= end):
#         return
#     tree[node] += diff
#     if start != end:
#         update(node*2, start, (start+end)//2, index, diff)
#         update(node*2 + 1, (start+end)//2 + 1, end, index, diff)

n,m = map(int,input().split())
l = list(map(int,input().split()))
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))

init(1, 0, n-1)

for i in range(m-1,n-m+1):
    left = i - (m-1)
    right = i + (m-1)
    print(subsum(1,0,n-1,left,right), end=' ')