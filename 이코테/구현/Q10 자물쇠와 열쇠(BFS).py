from collections import deque


def solution(key, lock):
    n = len(key)
    m = len(lock)

    def extract_coord(lst):
        result = []
        n = len(lst)
        for i in range(n):
            for j in range(n):
                if lst[i][j] == 1:
                    result.append((i, j))
        return result

    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                lock[i][j] = 1
            else:
                lock[i][j] = 0

    key_state = extract_coord(key)
    lock_state = extract_coord(lock)

    def rotate_clockwise(key):
        result = [[] for _ in range(n)]
        for lst in key:
            for i in range(n):
                result[i].append(lst[i])

        for i in range(len(result)):
            result[i] = result[i][::-1]
        return result

    def rotate_anti_clockwise(key):
        result = [[] for _ in range(n)]
        hash = {}
        end = n - 1
        for i in range(n):
            hash[i] = end
            end -= 1
        for lst in key:
            for i in range(n):
                index = hash[i]
                result[index].append(lst[i])
        return result

    def move(direction):
        coord_list = extract_coord(key)
        result = []
        if direction == 'up':
            for c in coord_list:
                tmp = (c[0] - 1, c[1])
                if tmp[0] >= 0:
                    result.append(tmp)
        elif direction == 'down':
            for c in coord_list:
                tmp = (c[0] + 1, c[1])
                if tmp[0] < n:
                    result.append(tmp)
        elif direction == 'left':
            for c in coord_list:
                tmp = (c[0], c[1] - 1)
                if tmp[1] >= 0:
                    result.append(tmp)
        else:
            for c in coord_list:
                tmp = (c[0], c[1] + 1)
                if tmp[1] < n:
                    result.append(tmp)
        key_result = [[0] * n for _ in range(n)]
        for c in result:
            key_result[c[0]][c[1]] += 1
        return key_result

    q = deque()
    q.append(key)
    visited = []
    visited.append(key)
    while q:
        x = q.popleft()

        x_state = extract_coord(x)
        num = 0
        for l in lock_state:
            if l in x_state:
                num += 1
        if num == len(lock_state):
            return True

        clock = rotate_clockwise(x)
        anti_clock = rotate_anti_clockwise(x)
        up = move('up')
        down = move('down')
        right = move('right')
        left = move('left')

        hash_val = {}
        hash_val['clock'] = clock
        hash_val['anti_clock'] = anti_clock
        hash_val['up'] = up
        hash_val['down'] = down
        hash_val['right'] = right
        hash_val['left'] = left
        dir_list = hash_val.keys()

        for k in dir_list:
            if hash_val[k] not in visited:
                visited.append(hash_val[k])
                q.append(hash_val[k])

    return False