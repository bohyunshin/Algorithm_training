from collections import defaultdict


def recursive(s, ans, index):
    if s == 'a':
        ans[index] = 1
        return True
    if (len(s) == 1 and s != 'a') or len(s) == 0:
        if ans[index] != 1:
            ans[index] = 0
        return False

    if s[0] == 'a':
        recursive(s[1:], ans, index)
    if s[-1] == 'a':
        recursive(s[:-1], ans, index)
    cnt = 0
    for i, j in zip(s, s[::-1]):
        if i == j == 'b':
            cnt += 1
        else:
            break
    if cnt >= 1:
        recursive(s[(cnt):(-cnt)], ans, index)

    return


def solution(a):
    ans = defaultdict(int)
    for index, i in enumerate(a):
        recursive(i, ans, int(index))
    final_ans = []
    for i in range(len(a)):
        if i not in ans.keys():
            final_ans.append(False)
        elif ans[i] == 0:
            final_ans.append(False)
        elif ans[i] == 1:
            final_ans.append(True)
    return final_ans