
def solution(n, k, cmd):
    answer = ''
    n = len(cmd)
    # myhash = {}
    # for i in range(n):
    #     myhash[i] = 0
    original = []
    copy = []
    q = []
    for i in range(n-1):
        # heapq.heappush(original, i)
        # heapq.heappush(copy, i)
        original.append(i)
        copy.append(i)

    for i in range(n):
        current_cmd = cmd[i]
        if 'D' in current_cmd or 'U' in current_cmd:
            direction, num = current_cmd.split(' ')
            if direction == 'D':
                k += int(num)
            else:
                k -= int(num)
        else:
            if current_cmd == 'C':
                q.append( (k,copy[k]) )
                before = len(copy)
                del copy[k]
                if k == before - 1:
                    k -= 1
            else:
                index, restore = q.pop()
                copy.insert(index, restore)
    answer = ['O']*n
    for i in q:
        answer[i[0]] = 'X'
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))