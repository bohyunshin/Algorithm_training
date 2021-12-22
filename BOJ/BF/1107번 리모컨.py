n = int(input())
LEN = len(str(n))
m = int(input())
if m == 0:
    buttons = [i for i in range(10)]
    breaks = []
else:
    breaks = list(map(int,input().split()))
    buttons = [i for i in range(10) if i not in breaks]
ans = 1e100
for i in range(1000000):
    FLAG = False
    for b in breaks:
        if str(b) in str(i):
            FLAG = True
            break
    if FLAG:
        tmp = abs(100-n)
    else:
        tmp = len(str(i))
        tmp += abs(n-i)
        tmp = min(tmp,abs(100-n))
    if ans > tmp:
        ans = tmp
print(ans)
# if n == 100:
#     print(0)
# else:
#     print(ans)

# candis = []
# c = [False]*len(buttons)
# a = [0]*LEN
# def go(index,LEN):
#     if index == LEN:
#         candis.append(int(''.join(list(map(str,a)))))
#         return
#     for i in range(len(buttons)):
#         if index == 0 and buttons[i] == 0:
#             if LEN > 1:
#                 continue
#         a[index] = buttons[i]
#         go(index+1,LEN)
# go(0,LEN)
# min_dist = 1e100
# channel = -1
# for candi in candis:
#     if abs(candi - n) < min_dist:
#         min_dist = abs(candi - n)
#         channel = candi
#
# path_A = len(str(channel)) + min_dist
# path_B = abs(100-n)
#
# print(min(path_A,path_B))