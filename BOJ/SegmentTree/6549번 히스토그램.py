import math, sys

input = sys.stdin.readline

# 아래의 설정을 해주지 않으면 최대 재귀 제한에 걸려 런타임 오류가 생긴다.
sys.setrecursionlimit(10 ** 6)


# 세그먼트 트리 생성
def init(arr, tree, node, start, end):
    if start == end:
        tree[node - 1] = start
    else:
        mid = (start + end) // 2
        init(arr, tree, node * 2, start, mid)
        init(arr, tree, node * 2 + 1, mid + 1, end)
        # node-1은 부모, node*2-1과 node*2는 각각 왼쪽, 오른쪽 자식노드를 의미

        if arr[tree[node * 2 - 1]] < arr[tree[node * 2]]:
            tree[node - 1] = tree[node * 2 - 1]
        else:
            tree[node - 1] = tree[node * 2]
            # 부모 노드에 더 작은 자식 노드를 입력


# 구간 최솟값을 찾아주는 쿼리 함수
def query(arr, tree, node, start, end, x, y):
    # 주어진 범위가 전체 범위를 벗어난 경우
    if x > end or y < start:
        return -1
    # 주어진 범위가 전체 범위 안에 포함되는 경우
    if start >= x and end <= y:
        return tree[node - 1]

    mid = (start + end) // 2
    left = query(arr, tree, node * 2, start, mid, x, y)
    right = query(arr, tree, node * 2 + 1, mid + 1, end, x, y)

    # 한쪽 노드가 범위를 벗어난 경우 자연스럽게 반대쪽 노드가 선택됨
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        # 더 작은 값의 인덱스 선택
        if arr[left] >= arr[right]:
            return right
        else:
            return left


def dac(start, end):
    # 해당 구간 범위의 최솟값 인덱스를 구함
    index = query(arr, tree, 1, 0, len(arr) - 1, start, end)

    # 단일 블럭인 경우
    if abs(end - start) == 0:
        return arr[index]

    # v1 = 가장 낮은 블럭의 높이 * 히스토그램의 길이
    v1, v2, v3 = arr[index] * (end - start + 1), 0, 0

    # 범위를 벗어나지 않는 경우 분할
    if index - 1 >= start:
        v2 = dac(start, index - 1)
    if index + 1 <= end:
        v3 = dac(index + 1, end)

    return max(v1, v2, v3)


while (True):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break

    n = temp[0]
    arr = temp[1:]
    tree = [0] * (pow(2, math.ceil(math.log(len(arr), 2)) + 1) - 1)
    # 편하게 n*4를 해도 되지만, 최적 길이로 생성하는 방법은 위와 같다

    init(arr, tree, 1, 0, len(arr) - 1)
    print(dac(0, len(arr) - 1))