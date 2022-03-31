from math import log2, ceil
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = [l[start],start]
        return tree[node]
    left = init(node*2, start, (start+end)//2)
    right = init(node*2 + 1, (start+end)//2 + 1, end)
    tree[node][0] = left[0] + right[0]
    if l[left[1]] > l[right[1]]:
        tree[node][1] = right[1]
    else:
        tree[node][1] = left[1]
    return tree[node][:]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node][0]
    if end < left or right < start:
        return 0
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)

def submin(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node][1]
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
    val = subsum(1,0,n-1,start,end) * l[idx]
    if start < idx:
        val = max(val, find_ans(start, idx-1))
    if idx < end:
        val = max(val, find_ans(idx+1, end))
    return val


n= int(input())
h = int(ceil(log2(n)))
tree = [[0,1e100] for _ in range(2**(h+1))]
l = list(map(int,input().split()))

init(1, 0, n-1)

print(find_ans(0,n-1))

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