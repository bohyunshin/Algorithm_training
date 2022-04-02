from math import log2, ceil
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    left = init(node*2, start, (start+end)//2)
    right = init(node*2 + 1, (start+end)//2 + 1, end)
    if l[left] > l[right]:
        tree[node] = right
    else:
        tree[node] = left
    return tree[node]

def submin(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return -1
    a = submin(node*2, start, (start+end)//2, left, right)
    b = submin(node*2 + 1, (start+end)//2 + 1, end, left, right)
    if a == -1:
        return b
    elif b == -1:
        return a
    else:
        if l[a] > l[b]:
            return b
        else:
            return a

def find_ans(start, end):
    idx = submin(1,0,n-1,start,end)
    val = l[idx]*(end-start+1)
    if start < idx:
        val = max(val, find_ans(start, idx-1))
    if idx < end:
        val = max(val, find_ans(idx+1, end))
    return val

while True:
    cur = list(map(int,input().split()))
    if cur[0] == 0:
        break
    n,l = cur[0], cur[1:]
    h = int(ceil(log2(n)))
    tree = [0]*(2**(h+1))

    init(1, 0, n-1)
    print(find_ans(0,n-1))
