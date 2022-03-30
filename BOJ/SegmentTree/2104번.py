from math import log2, ceil
import sys
input = sys.stdin.readline

def init_sum(node, start, end):
    global ans
    if start == end:
        tree[node] = [l[start],l[start]]
        ans.append(tree[node][0]*tree[node][1])
        return tree[node]
    left = init_sum(node*2, start, (start+end)//2)
    right = init_sum(node*2 + 1, (start+end)//2 + 1, end)
    print(left,right)
    tree[node][0] = left[0] + right[0]
    tree[node][1] = min(left[1], right[1])
    ans.append(tree[node][0]*tree[node][1])
    return tree[node][:]

# def init_min(node, start, end):
#     if start == end:
#         tree_min[node] = l[start]
#         return tree_min[node]
#     tree_min[node] = min(init_min(node*2, start, (start+end)//2), init_min(node*2 + 1, (start+end)//2 + 1, end))
#     return tree_min[node]

# def subsum(node, start, end, left, right):
#     if left <= start and end <= right:
#         return tree_sum[node]
#     if end < left or right < start:
#         return 0
#     return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2 + 1, (start+end)//2 + 1, end, left, right)
#
# def submin(node, start, end, left, right):
#     if left <= start and end <= right:
#         return tree_min[node]
#     if end < left or right < start:
#         return 0
#     return submin(node*2, start, (start+end)//2, left, right) + submin(node*2 + 1, (start+end)//2 + 1, end, left, right)
#
# def find_ans(node, start, end):
#     global ans
#     val = tree_sum[node]*tree_min[node]
#     ans = max(val, ans)
#     if start == end:
#         return
#     find_ans(node * 2, start, (start + end) // 2)
#     find_ans(node * 2 + 1, (start + end) // 2 + 1, end)




n= int(input())
h = int(ceil(log2(n)))
tree_sum = [0]*(2**(h+1))
tree_min = [0]*(2**(h+1))
tree = [[0,1e100] for _ in range(2**(h+1))]
l = list(map(int,input().split()))

ans = []
init_sum(1, 0, n-1)
print(ans)
print(tree)

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