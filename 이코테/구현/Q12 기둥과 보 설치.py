def solution(n, build_frame):
    answer = []
    gidoong = []
    bo = []

    def remove_gidoong(x, y):

        if (x, y) not in gidoong:
            return
        index = gidoong.index((x, y))
        del gidoong[index]

    def remove_bo(x, y):

        if (x, y) not in bo:
            return
        index = bo.index((x, y))
        del bo[index]

    for work in build_frame:
        x, y, a, b = work

        # 기둥을 짓는 제약 조건
        # 맨 아래에 있거나 기둥의 아래에 보 또는 기둥이 있어야 함
        # 기둥 설치인 경우
        if a == 0 and b == 1:
            if y == 0:
                gidoong.append((x, y))
            elif y != 0 and (x, y - 1) in gidoong:
                gidoong.append((x, y))
            elif (x, y) in bo or (x - 1, y) in bo:
                gidoong.append((x, y))
        # 보 설치인 경우
        elif a == 1 and b == 1:
            # 보의 한쪽 끝이 기둥과 닿아있거나
            # 보의 양쪽 끝이 또 다른 보와 닿아있어야 한다.
            if (x, y - 1) in gidoong or (x + 1, y - 1) in gidoong or ((x - 1, y) in bo and (x + 1, y) in bo):
                bo.append((x, y))
        # 기둥 삭제인 경우
        elif a == 0 and b == 0:
            # 삭제하려는 기둥 위에는 기둥이 있다면 보가 있어야 함
            # 그럴 때만 기둥을 삭제할 수 있다.
            if (x, y + 1) in gidoong and ((x, y + 1) in bo or (x - 1, y + 1) in bo):
                remove_gidoong(x, y)
            # 삭제하려는 기둥 기준으로 왼쪽에만 보가 있다면
            if (x - 1, y + 1) in bo and (x, y + 1) not in bo:
                # 이때는 반드시 왼쪽 보에 반드시 기둥이 있어야 함
                if (x - 1, y) in gidoong:
                    remove_gidoong(x, y)
            # 삭제하려는 기둥 기준으로 오른쪽에만 보가 있다면
            if (x, y + 1) in bo and (x - 1, y + 1) not in bo:
                # 이때는 반드시 오른쪽 보에 반드시 기둥이 있어야 함
                if (x + 1, y) in gidoong:
                    remove_gidoong(x, y)
            # 삭제하려는 기둥 양쪽으로 보가 있다면
            if (x - 1, y + 1) in bo and (x, y + 1) in bo:
                # 양쪽 보 중 하나가 없거나 둘다 연결되어 있거나
                if (x - 1, y) in gidoong or (x + 1, y) in gidoong or (x - 2, y + 1) in bo or (x + 1, y + 1) in bo:
                    remove_gidoong(x, y)
        # 보 삭제인 경우
        elif a == 1 and b == 0:
            # 삭제한 보 양 옆에 보가 있다면
            if (x - 1, y) in bo and (x + 1, y) in bo:
                # 삭제하려는 보 위에 기둥이 아무것도 없다면
                if (x, y) not in gidoong and (x + 1, y) not in gidoong:
                    # 둘 중 하나라도 기둥이 없으면 얘는 못 없앤다.
                    if ((x - 1, y - 1) in gidoong or (x, y - 1) in gidoong) and (
                            (x + 1, y - 1) in gidoong or (x + 2, y - 1) in gidoong):
                        remove_bo(x, y)
                # 삭제하려는 보 왼쪽에만 기둥이 있고 오른쪽에는 없으면
                elif (x, y) in gidoong and (x + 1, y) not in gidoong:
                    if ((x - 1, y - 1) in gidoong or (x, y - 1) in gidoong) and (
                            (x + 1, y - 1) in gidoong or (x + 2, y - 1) in gidoong):
                        remove_bo(x, y)
                # 삭제하려는 보 오른쪽에만 기둥이 있고 왼쪽에는 없으면
                elif (x, y) not in gidoong and (x + 1, y) in gidoong:
                    if ((x - 1, y - 1) in gidoong or (x, y - 1) in gidoong) and (
                            (x, y) in gidoong or (x + 1, y) in gidoong or (x + 2, y) in gidoong):
                        remove_bo(x, y)
                # 삭제하려는 보 양쪽에 기둥이 있다면
                else:
                    if ((x - 1, y - 1) in gidoong or (x, y - 1) in gidoong) and (
                            (x, y) in gidoong or (x + 1, y) in gidoong or (x + 2, y) in gidoong):
                        remove_bo(x, y)

        else:
            pass

    for g in gidoong:
        x, y = g
        answer.append([x, y, 0])
    for b in bo:
        x, y = b
        answer.append([x, y, 1])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer