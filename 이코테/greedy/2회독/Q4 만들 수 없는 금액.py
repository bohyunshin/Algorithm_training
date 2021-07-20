n = int(input())
array = list(map(int, input().split()))
# array.sort(reverse=True)
#
# # result = 0
# # money = 1
# # while True:
# #     money_copy = money
# #     for coin in array:
# #         if coin > money:
# #             continue
# #         elif money_copy - coin >= 0:
# #             money_copy -= coin
# #         if money_copy == 0:
# #             break
# #     if money_copy != 0:
# #         result = money
# #         break
# #     else:
# #         money += 1
# # print(result)

target = 1
array.sort()
for i in array:
    if i > target:
        break
    target += i
print(target)