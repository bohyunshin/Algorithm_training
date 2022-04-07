from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]
    tree[node] = init(node*2, start, (start+end)//2) + init(node*2 + 1, (start+end)//2+1, end)
    return tree[node]

def query(node, start, end, k):
    tree[node] -= 1
    if start == end:
        # print(start+1)
        return start
    if node*2 <= tree_size-1 and tree[node*2] > k:
        return query(node*2, start, (start+end)//2, k)
    k -= tree[node*2]
    if node*2 + 1 <= tree_size-1 and tree[node*2 + 1] > k:
        return query(node*2 + 1, (start+end)//2 + 1, end, k)

def update(node, start, end, index, diff=-1):
    if not (start <= index <= end):
        return
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2 + 1, (start+end)//2 + 1, end, index, diff)

# def update(node, start, end, index):
#     if not (start <= index <= end):
#         return
#     if start == end:
#         tree[node] = 0
#         return
#     update(node*2, start, (start+end)//2, index)
#     update(node*2 + 1, (start+end)//2 + 1, end, index)
#     tree[node] -= 1

n = int(input())
h = int(ceil(log2(n)))
tree = [0]*(2**(h+1))
# tree = [0]*(4*n)
tree_size = len(tree)
l = [0]*(n)

init(1,0,n-1)

for i in range(1,n+1):
    k = int(input())
    x = query(1,0,n-1,k)
    # print(i,x)
    l[x] = str(i)
    # update(1,0,n-1,x)

print('\n'.join(l))