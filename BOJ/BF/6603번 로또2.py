from itertools import combinations

result = []
while True:
    lst = list(map(int, input().split()))
    # while 끝내는 조건
    if lst[0] == 0:
        break
    # 입력 받음
    k, number = lst[0], lst[1:]
    # combinations 사용
    # 어차피 사전순이라서 그대로 가져다 쓰면 됨.
    for c in combinations(number, 6):
        result.append(c)

    result.append('')

for c in result:
    print(' '.join([str(i) for i in c]))