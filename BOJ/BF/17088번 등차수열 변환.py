n = int(input())
a = list(map(int,input().split()))
if n <= 2:
    print(0)
else:
    ans = 1e100
    dx = [0,1,-1]
    # 0이면 연산 안한 것, 1이거나 -1이면 연산 한 것을 기록하기 위한 딕셔너리.
    dct = {0:0,1:1,2:1}
    # 첫째항과 둘째항을 돌면서 9가지 경우에 대해 최솟값을 구해본다.
    for i in range(3):
        first = a[0] + dx[i]
        for j in range(3):
            second = a[1] + dx[j]
            # 정답과 비교하는, 연산을 몇회했는지 기록하는 변수.
            tmp = dct[i] + dct[j]
            # 등차를 만들기 위해 이전 항을 기록하는 변수.
            before = second
            # 끝까지 갔는지를 기록하는 변수.
            end = True
            # 첫번째 항과 두번째 항의 차이
            if first >= second:
                greater = 1
                b = first-second
            else:
                greater = 0
                b = second-first
            for k in range(2,n):
                FLAG = False
                x = a[k]
                for l in range(3):
                    nx = x+dx[l]
                    # 등차수열이 되는 경우.
                    if (before >= nx and greater == 1 and before-nx == b) or \
                            (before < nx and greater == 0 and nx-before == b):
                        FLAG = True
                        tmp += dct[l]
                        before = nx
                    if FLAG:
                        break
                # 이 조건에서 걸리면 끝까지 못갔다는 것이니까,
                # end = False로 잡아주고 루프에서 빠져나옴.
                if FLAG == False:
                    end = False
                    break
            # 이 조건에서 걸리면 끝까지 갔다느 것이니까,
            # 정답을 업데이트해줌.
            if end:
                ans = min(ans,tmp)
    print(ans if ans != 1e100 else -1)