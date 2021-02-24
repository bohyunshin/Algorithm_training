def possible(answer):
    for x,y,work in answer:
        # 기둥이라면
        if work == 0:
            # 맨 바닥에 있거나 아래에 기둥이 있거나 보의 한쪽 위에 있거나
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            else:
                return False
        # 보라면
        elif work == 1:
            # 한쪽이 기둥과 닿아 있거나 양쪽이 보와 연결되어 있다면
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ( [x-1,y,1] in answer and [x+1,y,1] in answer ):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        # 설치라면
        if b == 1:
            # 우선 정답에 추가해보고
            # possible 함수 결과에 따라서 다시 뺀다.
            answer.append([x,y,a])
            if possible(answer):
                continue
            else:
                answer.remove([x,y,a])
        # 삭제라면
        elif b == 0:
            # 우선 삭제해보고
            # possible 함수 결과에 따라서 다시 추가해본다.
            answer.remove([x,y,a])
            if possible(answer):
                continue
            else:
                answer.append([x,y,a])
    return sorted(answer, key=lambda x: (x[0],x[1],x[2]))