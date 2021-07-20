n = int(input())
money = list(map(int,input().split()))
money.sort()

pay = 1

# while True:
#     original = pay
#     for m in money:
#         if pay-m < 0:
#             continue
#         elif pay-m > 0:
#             pay -= m
#         else:
#             pay -= m
#             break
#     if pay != 0:
#         print(original)
#         break
#     else:
#         pay = original+1

target = 1
for x in money:
    if target < x:
        break
    else:
        target += x
print(target)