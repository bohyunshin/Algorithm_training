from itertools import permutations
dice = [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
# dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
ans = []
def recursive(x,start,n):
    if 1 <= len(x) <= n:
        for p in permutations(x):
            if p[0] != 0:
                ans.append(''.join(list(map(str,p))))
    if len(x) > n:
        return
    for i in range(start,n):
        for j in range(len(dice[i])):
            recursive(x + [dice[i][j]], i+1, n)
            recursive(x, i+1, n)

recursive([],0,len(dice))
final_ans = sorted(map(int, list(set(ans))))
print(final_ans)
for i in range(len(final_ans)-1):
    if final_ans[i] + 1 != final_ans[i+1]:
        print(final_ans[i]+1)
        break