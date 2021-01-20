n = int(input())

count = 0
for i in range(60):
    if '3' in str(i):
        count += 1

result = 0
for i in range(n+1):
    if '3' in str(i):
        # 시각에 3이 들어가 있는 경우는
        # 모두 카운트 해준다
        result += 60*60
    else:
        # 시각에 3이 들어가 있지 않은 경우는
        # 분, 초를 따져주는데
        # 분에 3이 들어가있을 때 초는 아무거나 와도됨
        # 초에 3이 들어가있을 때 분은 아무거나 와도 됨
        # 둘 모두 3이 들어가있는 경우, 겹치므로 빼줘야 함
        result += count * 60 * 2
        result -= count * count
print(count, result)