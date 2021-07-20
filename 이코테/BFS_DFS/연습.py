from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9
start = 1
def dfs():
    s = []
    # print(start, end=' ')
    visited[start] = True
    print(start)
    s.append(start)
    x = start
    while s:
        all_visited = 0
        for neighbor in graph[x]:

            if visited[neighbor] is False:
                visited[neighbor] = True
                s.append(neighbor)
                print(neighbor)
                break
            else:
                all_visited += 1

        if all_visited == len(graph[x]):
            s.pop()
            try:
                x = s[-1]
            except:
                pass
            continue
        else:
            x = s[-1]

def dfs2(v):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if visited[neighbor] is False:
            dfs2(neighbor)

def bfs():
    q = deque([start])
    visited[start] = True
    print(start,end=' ')
    while q:
        x = q.popleft()
        for neighbor in graph[x]:
            if visited[neighbor] is False:
                visited[neighbor] = True
                print(neighbor,end=' ')
                q.append(neighbor)


def dfs_iteration():
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [start]

    while (stack):
        print(stack)
        # 스택에 남은것이 없을 때까지 반복
        node = stack.pop()  # node : 현재 방문하고 있는 꼭지점

        # 현재 node가 방문한 적 없다 -> visited에 추가한다.
        # 그리고 해당 node의 자식 node들을 stack에 추가한다.
        if (node not in visited):
            visited.append(node)
            # print(node)
            stack.extend(graph[node])
    return visited

def dfs_iter():
    s = []
    s.append(start)
    while s:
        node = s.pop()
        child = graph[node]
        if visited[node] is False:
            visited[node] = True
            s.extend(child)
            print(node)
dfs_iter()
