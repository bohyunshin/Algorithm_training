import sys

input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node][0] = array[start]
        tree[node][1] = array[start]
        return tree[node][:]

    mid = (start + end) // 2
    left = init(start, mid, node * 2)
    right = init(mid + 1, end, node * 2 + 1)
    tree[node][0] = min(left[0], right[0])
    tree[node][1] = max(left[1], right[1])
    return tree[node][:]

def summit(start, end, node, left, right):
    if left > end or right < start:
        return [1e100,-1e100]

    if left <= start and end <= right:
        return tree[node][:]

    mid = (start + end) // 2
    left_result = summit(start, mid, node * 2, left, right)
    right_result = summit(mid + 1, end, node * 2 + 1, left, right)
    return min(left_result[0],right_result[0]), max(left_result[1], right_result[1])


# def update(start, end, node, index, dif):
#     if index < start or index > end:
#         return
#
#     tree[node] += dif
#     if start == end:
#         return
#
#     mid = (start + end) // 2
#     update(start, mid, node * 2, index, dif)
#     update(mid + 1, end, node * 2 + 1, index, dif)


N, M= map(int, input().rstrip().split())

array = []
tree = [[1e100,-1e100] for _ in range((4 * N))]

for i in range(N):
    array.append(int(input().rstrip()))

init(0, N - 1, 1)

for i in range(M):
    a,b = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    MIN,MAX = summit(0,N-1,1,a,b)
    print(MIN,MAX)