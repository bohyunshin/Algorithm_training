# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    step = 3
    n = len(S)
    result = 0

    # in case S is lower than 3
    if n <= 2:
        if 'X' in S:
            return 1
        else:
            return 0

    index = 0
    while True:
        seg = S[index:index+step]
        # if first segment is good
        # we do not have to patch machine
        if seg[0] == '.':
            index += 1
        else:
            result += 1
            index += step
        if index >= len(S)-2:
            break
    # check rest of segments
    if 'X' in S[index:]:
        result += 1
    return result

    # for j in range(0,n-1,step):
    #     seg = S[j:j+step]
    #     if 'X' in seg:
    #         result += 1
    #     else:
    #         continue
    # # check rest of segments
    # if 'X' in S[j+step:]:
    #     result += 1
    # return result

