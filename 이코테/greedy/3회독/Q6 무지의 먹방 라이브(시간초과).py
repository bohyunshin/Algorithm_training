import heapq


def solution(food_times, k):
    index = 0
    time = 0

    while True:

        if sum(food_times) == 0:
            return -1

        if time == k:
            if food_times[index] == 0:
                if index == len(food_times) - 1:
                    index = 0
                    continue
                else:
                    index += 1
                    continue
            else:
                return index + 1

        if food_times[index] == 0:
            if index == len(food_times) - 1:
                index = 0
            else:
                index += 1
            continue
        else:
            food_times[index] -= 1
            if index == len(food_times) - 1:
                index = 0
            else:
                index += 1
        time += 1



