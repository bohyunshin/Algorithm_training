stringA = input()
stringB = input()

answer = 0
visited = [[0]*len(stringB) for _ in range(len(stringA))]

for i in range(len(stringA)):
    for j in range(len(stringB)):
        # 공통 부분 문자열이 시작하는 곳에서
        # 이미 방문한 적이 있으면 제외
        if stringA[i] == stringB[j] and visited[i][j] == 0:
            result = 0
            # 시작 지점에서부터 각 지점의 문자열을 비교해서 똑같으면 1을 더해줌
            for index, (a,b) in enumerate(zip(stringA[i:], stringB[j:])):
                if a == b:
                    result += 1
                    visited[i+index][j+index] += 1
                else:
                    break
            if answer < result:
                answer = result
print(answer)