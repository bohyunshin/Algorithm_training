from math import log2, ceil
import sys
input = sys.stdin.readline

# def init(node, start, end):
#     if start == end:
#         tree[node] = l[start]
#         return tree[node]
#     tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2 + 1, end)
#     return tree[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return 0
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)

def update(node, start, end, index):
    if not (start <= index <= end):
        return
    elif start == end:
        tree[node] += 1
        return
    update(node*2, start, (start+end)//2, index)
    update(node*2 + 1, (start+end)//2 + 1, end, index)
    tree[node] = tree[node*2] + tree[node*2 + 1]



n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_hash = {}
b_hash = {}
for i in range(n):
    a_hash[a[i]] = i
    b_hash[b[i]] = i
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
# init(1, 0, n-1)
ans = 0
for i in range(n):
    a_val = a[i]
    b_idx = b_hash[a_val]
    update(1,0,n-1,b_idx)
    ans += subsum(1,0,n-1,b_idx+1,n-1)
print(ans)


"""
5
132 392 311 351 231
231 351 311 392 132
"""