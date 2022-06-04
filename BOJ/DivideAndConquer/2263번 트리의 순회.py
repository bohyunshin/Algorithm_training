import sys
sys.setrecursionlimit(10**6)
n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
# position[i]: i번 정점이 인오더에서 몇번째인지 나타낸다.
# in_order[position[i]] -> i
position = [-1]*(n+1)
for idx,node in enumerate(in_order):
    position[node] = idx
pre_order = []
def traversal(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = post_order[post_end]
    pre_order.append(root)
    p = position[root]

    # in_order: in_start p in_end
    # post_order: post_start, post_end(=p)
    # left: p-in_start
    # > (in_start ~ p-1까지의 노드 수 = 왼쪽 자식의 수)
    # right: in_end-p
    # > (p+1 ~ in_end까지의 노드 수 = 오른쪽 자식의 수)
    left = p-in_start
    right = in_end-p
    # left side
    traversal(in_start, p-1, post_start, post_start+left-1)
    # right side
    traversal(p+1, in_end, post_start+left, post_end-1)
traversal(0,n-1,0,n-1)
print(' '.join(map(str,pre_order)))
