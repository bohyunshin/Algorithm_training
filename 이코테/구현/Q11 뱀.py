n = int(input())
k = int(input())
apple = []
for _ in range(k):
    r,c = map(int, input().split())
    apple.append((r,c))
l = int(input())
direction = []
for _ in range(l):
    x,c = input().split()
    direction.append((int(x),c))
direction_hash = {}
for i in direction:
    direction_hash[i[0]] = i[1]

snake_head = (1,1)
snake_tail = (1,1)
snake_body = [(1,1)]
head = 'right'
def move_coord(c, head):
    if head == 'right':
        result = (c[0], c[1]+1)
    elif head == 'left':
        result = (c[0], c[1]-1)
    elif head == 'down':
        result = (c[0]+1, c[1])
    else:
        result = (c[0]-1, c[1])
    return result
def move_head(c, head):
    global snake_body
    result = move_coord(c, head)
    if result[0] < 1 or result[0] > n or result[1] < 1 or result[1] > n or result in snake_body:
        return 'game over'
    else:
        return result
def move_tail(c, snake_head, head):
    global length
    if snake_head not in apple:
        result = move_coord(c, head)
    else:
        length += 1
        # 먹은 사과 없애기
        index = apple.index(snake_head)
        del apple[index]
        result = c
    return result
def turn(head, which):
    if head == 'right':
        if which == 'L':
            return 'up'
        else:
            return 'down'
    elif head == 'left':
        if which == 'L':
            return 'down'
        else:
            return 'up'
    elif head == 'up':
        if which == 'L':
            return 'left'
        else:
            return 'right'
    else:
        if which == 'L':
            return 'right'
        else:
            return 'left'

time = 0
length = 1
trail = [(1,1)]

while True:

    if snake_head == 'game over':
        print(time)
        break

    time += 1
    snake_head = move_head(snake_head, head)
    trail.append(snake_head)
    snake_body = trail[-length:]
    snake_tail = move_tail(snake_tail, snake_head, head)



    if time in direction_hash.keys():
        which = direction_hash[time]
        head = turn(head, which)

    # print(snake_head, snake_tail, snake_body)

"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""


"""
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
"""