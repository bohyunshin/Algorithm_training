from math import log2, ceil
import sys
input = sys.stdin.readline

def init_sum(node, start, end):
    if start == end:
        tree_sum[node] = l[start]
        return tree_sum[node]
    tree_sum[node] = init_sum(node*2, start, (start+end)//2) + init_sum(node*2 + 1, (start+end)//2 + 1, end)
    return tree_sum[node]

def init_min(node, start, end):
    if start == end:
        tree_min[node] = l[start]
        return tree_min[node]
    tree_min[node] = min(init_min(node*2, start, (start+end)//2), init_min(node*2 + 1, (start+end)//2 + 1, end))
    return tree_min[node]

def subsum(node, start, end, left, right):
    if left <= start and end <= right:
        return tree_sum[node]
    if end < left or right < start:
        return 0
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)

def submin(node, start, end, left, right):
    if left <= start and end <= right:
        return tree_min[node]
    if end < left or right < start:
        return 0
    return submin(node*2, start, (start+end)//2, left, right) + submin(node*2 + 1, (start+end)//2 + 1, end, left, right)

def find_ans(node, start, end):
    global ans
    val = tree_sum[node]*tree_min[node]
    ans = max(val, ans)
    if start == end:
        return
    find_ans(node * 2, start, (start + end) // 2)
    find_ans(node * 2 + 1, (start + end) // 2 + 1, end)




n= int(input())
h = int(ceil(log2(n)))
tree_sum = [0]*(2**(h+1))
tree_min = [0]*(2**(h+1))
l = list(map(int,input().split()))

init_sum(1, 0, n-1)
init_min(1, 0, n-1)

ans = -1


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