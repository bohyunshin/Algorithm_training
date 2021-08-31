from itertools import permutations


def recursive(x, start, n, dice, ans):
    if 1 <= len(x) <= n:
        for p in permutations(x):
            if p[0] != 0:
                ans.append(''.join(list(map(str, p))))
    if len(x) > n:
        return
    for i in range(start, n):
        for j in range(len(dice[i])):
            recursive(x + [dice[i][j]], i + 1, n, dice, ans)
            recursive(x, i + 1, n, dice, ans)


def solution(dice):
    ans = []
    recursive([], 0, len(dice), dice, ans)
    final_ans = sorted(map(int, list(set(ans))))
    for i in range(len(final_ans) - 1):
        if final_ans[i] + 1 != final_ans[i + 1]:
            return final_ans[i] + 1