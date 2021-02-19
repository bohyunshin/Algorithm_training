def solution(food_times, k):
    index = 0
    times = 0
    while True:
        # index 찾기
        while food_times[index] == 0:
            if index == len(food_times) - 1:
                index = 0
            else:
                index += 1

        food_times[index] -= 1
        times += 1

        if index == len(food_times) - 1:
            index = 0
        else:
            index += 1

        if times == k:
            if sum(food_times) == 0:
                return -1
            else:
                while food_times[index] == 0:
                    if index == len(food_times) - 1:
                        index = 0
                    else:
                        index += 1
                return index + 1
