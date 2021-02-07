# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 함수를 호출함
    # 루트노드의 기준은 노드 번호 = 부모의 노드 번호
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        # a의 노드 번호가 작다면
        # b가 a를 바라보도록 = b의 부모 노드를 a로 정한다
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

# union 연산을 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
# 결국 부모 노드를 호출하는데, 재귀적으로 부모 노드를 호출하니까
# 동일한 루트 노드를 가지는 애들은 동일한 그룹이라고 판단함
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')
print()

# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=' ')