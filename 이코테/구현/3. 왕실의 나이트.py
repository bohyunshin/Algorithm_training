current = input()

y_label = ['a','b','c','d','e','f','g','h']
x, y = int(current[1]), y_label.index(current[0]) + 1

# 모든 경우의수: 나이트는 총 8개가지수로 움직일 수 있다.
dx = [1,-1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,1,-1]

result = []
for dx_, dy_ in zip(dx,dy):
    nx = x + dx_
    ny = y + dy_
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        result.append(y_label[ny-1] + str(nx))
print(result)