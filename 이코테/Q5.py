# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

sys.setrecursionlimit(10 ** 7)


def solution(S):
    S_after = S.replace('AB', '')
    S_after = S_after.replace('BA', '')
    S_after = S_after.replace('CD', '')
    S_after = S_after.replace('DC', '')
    # print(S, S_after)

    if S == S_after:
        return S_after
    else:
        solution(S_after)

    return S_after

    # index = 0
    # surviving_index = []
    # FLAG = False
    # while True:
    #     s = S[index:index+2]
    #     # check whether transformation is possible
    #     if s in ['AB','BA','CD','DC']:
    #         index += 2
    #     else:
    #         surviving_index.append(index)
    #         index += 1
    #         FLAG = True
    #     if index >= len(S)-1:
    #         break
    # print(index, len(S))
    # if index == len(S)-1:
    #     result = S[index]
    # else:
    #     result = ''
    # for i in surviving_index:
    #     result += S[i]
    # print(result)


