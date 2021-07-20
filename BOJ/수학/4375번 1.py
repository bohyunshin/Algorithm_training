while True:
    try:
        x = int(input())
    except:
        break

    answer = 1
    mod = answer % x

    while True:
        if mod == 0:
            break
        mod = (mod * 10 + 1) % x
        answer += 1
    print(answer)

    # find_answer = False
    # answer = '1'
    # while True:
    #     if int(answer) % x == 0:
    #         find_answer = True
    #         break
    #     else:
    #         answer += '1'
    #
    # if find_answer:
    #     print(len(answer))