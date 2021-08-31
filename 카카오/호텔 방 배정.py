from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def solution(k, room_number):
    dct = defaultdict(int)
    used = [False] * (k + 1)
    ans = []
    for room in room_number:
        if used[room] == False:
            used[room] = True

            # v = room+1
            # tmp = [v]
            # while used[v] == True:
            #     v = dct[v]
            #     tmp.append(v)
            dct[room] = room + 1

            ans.append(room)
        else:
            alter = dct[room]
            tmp = []
            tmp.append(alter)
            while used[alter] == True:
                alter = dct[alter]
                tmp.append(alter)
            used[alter] = True

            for v in tmp:
                dct[v] = alter + 1

            # v = alter+1
            # while used[v] == True:
            #     v = dct[v]
            # dct[alter] = v

            ans.append(alter)
    return ans