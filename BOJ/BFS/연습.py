def check(dct, n):
    for key in dct.keys():
        x, y = key
        # 기둥, 보 둘다 없으면 확인할 필요 없음.
        if dct[key][0] == 0 and dct[key][1] == 0:
            continue
        # 기둥이 조건에 맞는지 확인
        if dct[key][0] == 1:
            # 기둥이 바닥에 있거나, 기둥 밑에 보가 있거나 기둥 위에 있으면 괜찮.
            if y == 0:
                continue
            # 기둥 아래에 기둥이 있을때도 오키
            if y >= 1 and dct[(x, y - 1)][0] == 1:
                continue
            # 기둥이 왼쪽 끝에 있다면
            if x == 0:
                if dct[(x, y)][1] == 1:
                    continue
                else:
                    return False
            elif x == n:
                if dct[(x - 1, y)][1] == 1:
                    continue
                else:
                    return False
            else:
                if dct[(x - 1, y)][1] == 1 or dct[(x, y)][1] == 1:
                    continue
                else:
                    return False
        # 보가 조건에 맞는지 확인
        if dct[key][1] == 1:
            # 보 양 옆 중 하나가 기둥에 걸쳐있거나, 보 양 옆 모두가 보에 연결되어 있으면 괜찮.
            # 우선 양 옆 중 하나가 기둥에 걸쳐있는 경우 체크
            if (dct[(x, y - 1)][0] == 1 or dct[(x + 1, y - 1)][0] == 1):
                continue
            # 위에서 체크했는데 보가 왼쪽 끝에 있거나 오른쪽 끝에 있으면 불가능한 경우임.
            if x == 0 or x == n - 1:
                return False
            else:
                if dct[(x - 1, y)][1] == 1 and dct[(x + 1, y)][1] == 1:
                    continue
                else:
                    False
    return True


def solution(n, build_frame):
    dct = {}
    ans = []
    for i in range(n + 1):
        for j in range(n + 1):
            dct[(i, j)] = {0: 0, 1: 0}
    for x, y, a, b in build_frame:

        if b == 1:
            # 설치 해봄
            dct[(x, y)][a] += 1
            # 확인 후 괜찮으면 ㄲ, 이상하면 다시 삭제함.
            if check(dct, n) == False:
                dct[(x, y)][a] -= 1

        elif b == 0:
            # 삭제 해봄
            dct[(x, y)][a] -= 1
            # 확인후 괜찮으면 ㄲ, 이상하면 다시 설치함.
            if check(dct, n) == False:
                dct[(x, y)][a] += 1

    for key in dct.keys():
        x, y = key
        # 기둥 있는지 확인
        if dct[key][0] == 1:
            ans.append([x, y, 0])
        # 보 있는지 확인
        if dct[key][1] == 1:
            ans.append([x, y, 1])
    ans.sort(key=lambda x: (x[0], x[1], x[2]))
    return ans

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
solution(n,build_frame)
