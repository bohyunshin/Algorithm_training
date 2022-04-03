from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, start_x, start_y, end_x, end_y):
    if (start_x,start_y) == (end_x,end_y):
        tree[node] = l[start_x][start_y]
        return tree[node]
    tree[node] = init(node*4, start_x, start_y, (start_x+end_x)//2, (start_y+end_y)//2) + \
                 init(node*4+1, start_x, (start_y+end_y)//2 + 1, (start_x+end_x)//2, end_y) + \
                 init(node*4+2, (start_x+end_x)//2 + 1, start_y, end_x, (start_y+end_y)//2) + \
                 init(node*4+3, (start_x+end_x)//2 + 1, (start_y+end_y)//2 + 1, end_x, end_y)
    return tree[node]

def subsum(node, start, end, left, right):
    start_x, start_y = start
    end_x, end_y = end
    left_x, left_y = left
    right_x, right_y = right
    if left_x <= start_x <= end_x <= right_x and \
        left_y <= start_y <= end_y <= right_y:
        return tree[node]
    if right_x < start_x or end_x < left_x or \
        right_y < start_y or end_y < left_y:
        return 0
    return subsum(node*4, (start_x, start_y), ((start_x+end_x)//2, (start_y+end_y)//2), left, right) + \
           subsum(node*4+1, (start_x, (start_y+end_y)//2 + 1), ((start_x+end_x)//2, end_y), left, right) + \
           subsum(node*4+2, ((start_x+end_x)//2 + 1, start_y), (end_x, (start_y+end_y)//2), left, right) + \
           subsum(node*4+3, ((start_x+end_x)//2 + 1, (start_y+end_y)//2 + 1), (end_x, end_y), left, right)

def update(node, start, end, idx, diff):
    start_x,start_y = start
    end_x,end_y = end
    idx_x,idx_y = idx
    if not (start_x <= idx_x <= end_x and start_y <= idx_y <= end_y):
        return
    tree[node] += diff
    if start != end:
        update(node * 4, (start_x, start_y), ((start_x + end_x) // 2, (start_y + end_y) // 2), idx, diff)
        update(node * 4 + 1, (start_x, (start_y + end_y) // 2 + 1), ((start_x + end_x) // 2, end_y), idx, diff)
        update(node * 4 + 2, ((start_x + end_x) // 2 + 1, start_y), (end_x, (start_y + end_y) // 2), idx, diff)
        update(node * 4 + 3, ((start_x + end_x) // 2 + 1, (start_y + end_y) // 2 + 1), (end_x, end_y), idx, diff)



n,m = map(int,input().split())
h = int(ceil(log2(n**2)))
tree = [0]*(2**(h+1))
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))

init(1, 0, 0, n-1, n-1)

for _ in range(m):
    cur = list(map(int,input().split()))
    if cur[0] == 1:
        _,x1,y1,x2,y2 = cur
        print(subsum(1,(0,0),(n-1,n-1),(x1-1,y1-1),(x2-1,y2-1)))
    else:
        _,x,y,c = cur
        diff = c-l[x-1][y-1]
        l[x-1][y-1] = c
        update(1,(0,0),(n-1,n-1),(x-1,y-1),diff)

"""
4 2
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
1 2 2 2 4
"""