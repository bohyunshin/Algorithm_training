from math import log2, ceil
import sys
input = sys.stdin.readline
def subsum(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    # if start == end:
    #     # tree[node] += 1
    #     return tree[node]
    return subsum(node*2, start, (start+end)//2, left, right) + \
           subsum(node*2+1, (start+end)//2 + 1, end, left, right)
def update(node, start, end, index):
    if not (start <= index <= end):
        return
    if start == end:
        tree[node] += 1
        return
    update(node*2, start, (start+end)//2, index)
    update(node*2+1, (start+end)//2+1, end, index)
    tree[node] = tree[node*2] + tree[node*2 + 1]
t = int(input())
for _ in range(t):
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
    ans = 0
    for i in range(n):
        aval = a[i]
        idx = b_hash[aval]
        update(1,0,n-1,idx)
        ans += subsum(1,0,n-1,idx+1,n-1)
    print(ans)