from math import ceil, log2
import sys
input = sys.stdin.readline

def xinit(ynode, start, end, xnode, yidx):
    if start == end:
        tree[ynode][xnode] = l[start][yidx]
        return tree[ynode][xnode]
    tree[ynode][xnode] = xinit(ynode, start, (start+end)//2, xnode*2, yidx) + \
                         xinit(ynode, (start + end) // 2 + 1, end, xnode * 2 + 1, yidx)
    return tree[ynode][xnode]

def yinit(ynode, start, end):
    if start == end:
        return xinit(ynode, 0, n-1, 1, start)
    yinit(ynode*2, start, (start+end)//2)
    yinit(ynode*2 + 1, (start+end)//2 + 1, end)
    for k in range(len(tree[0])):
        tree[ynode][k] = tree[ynode*2][k] + tree[ynode*2 + 1][k]

def xquery(ynode, xnode, start, end, left, right):
    if left <= start and end <= right:
        return tree[ynode][xnode]
    if end < left or right < start:
        return 0
    return xquery(ynode, xnode*2, start, (start+end)//2, left, right) + \
           xquery(ynode, xnode*2 + 1, (start + end) // 2 + 1, end, left, right)

def yquery(ynode, start, end, left, right, x1, x2):
    if left <= start and end <= right:
        return xquery(ynode, 1, 0, n-1, x1, x2)
    if end < left or right < start:
        return 0
    return yquery(ynode*2, start, (start+end)//2, left, right ,x1, x2) + \
           yquery(ynode*2 + 1, (start + end) // 2 + 1, end, left, right, x1, x2)

def xupdate(ynode, xnode, start, end, xidx, diff):
    if not (start <= xidx <= end):
        return
    tree[ynode][xnode] += diff
    if start != end:
        xupdate(ynode, xnode*2, start, (start+end)//2, xidx, diff)
        xupdate(ynode, xnode*2 + 1, (start+end)//2 + 1, end, xidx, diff)

def yupdate(ynode, start, end, yidx, xidx, diff):
    if not (start <= yidx <= end):
        return
    xupdate(ynode, 1, 0, n-1, xidx, diff)
    if start != end:
        yupdate(ynode*2, start, (start+end)//2, yidx, xidx, diff)
        yupdate(ynode*2 + 1, (start+end)//2+1, end, yidx, xidx, diff)

n,m = map(int,input().split())
h = int(ceil(log2(n)))
tree = [[0]*(2**(h+1)) for _ in range(2**(h+1))]
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))

yinit(1,0,n-1)

for _ in range(m):
    cur = list(map(int,input().split()))
    if cur[0] == 0:
        _,x,y,c = cur
        diff = c-l[x-1][y-1]
        l[x-1][y-1] = c
        yupdate(1,0,n-1,y-1,x-1,diff)
    else:
        _,x1,y1,x2,y2 = cur
        print(yquery(1, 0, n-1, y1-1, y2-1, x1-1, x2-1))