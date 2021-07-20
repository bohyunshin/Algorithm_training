# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # this solution is valid only if
    # we regard that zero is divisible by any interger number
    result = []
    # case when there is no change
    if int(S) % 3 == 0:
        result.append(S)
    # case when there is only one change
    for i in range(len(S)):
        for j in range(0,10):
            if i == 0:
                candi = str(j) + S[1:]
            elif i == len(S)-1:
                candi = S[:-1] + str(j)
            else:
                candi = S[:i] + str(j) + candi[i+1:]
            if int(candi) % 3 == 0:
                result.append(candi)
    return len(set(result))

