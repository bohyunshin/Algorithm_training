n,m = map(int, input().split())

s = []
result = []
def f():
    if len(s) == m:
        # result.append(' '.join(sorted(map(str,s))))
        print(' '.join((map(str, s))))
        return
    for i in range(1, n+1):
        # 만약에 현재 s = [1, 2]이고
        # 새로 들어오는 애가 3이면 얘는 받지 않음
        # '3 4'와 '4 3'가 이 문제에서는 동일한데
        # 이 둘을 모두 재귀에 넣지 않기 위한 로직임
        if sum(map(lambda x: x > i, s)) >= 1:
            continue
        s.append(i)
        f()
        s.pop()
f()
