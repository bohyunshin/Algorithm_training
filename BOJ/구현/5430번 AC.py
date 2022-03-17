t = int(input())
input_number = 0

while True:

    p = input()
    n = int(input())
    if n != 0:
        a = [int(i) for i in input()[1:-1].split(',')]
    else:
        a = input()
        a = []

    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
    else:
        flag = False
        R = 0
        INDEX = [0,n-1]
        for f in p:
            if f == 'R':
                R += 1
                INDEX = INDEX[::-1]
            else:
                if INDEX[0] == -100:
                    print('error')
                    flag = True
                    break
                if R % 2 == 0:
                    INDEX[0] += 1
                else:
                    INDEX[0] -= 1
            if (R % 2 == 0 and INDEX[0] - INDEX[1] == 2) or \
                (R % 2 == 1 and INDEX[1] - INDEX[0] == 2):
                INDEX = [-100,-100]

        if INDEX[0] != -100:
            ans = []
            if R % 2 == 0:
                for i in range(INDEX[0],INDEX[1]+1):
                    ans.append(a[i])
            else:
                for i in range(INDEX[0],INDEX[1]-1,-1):
                    ans.append(a[i])
            print('[' + ','.join(map(str,ans)) + ']')
        else:
            if flag == False:
                print('error')

    input_number += 3

    if input_number // 3 == t:
        break


"""
1
RRRRRDDDD
4
[1,2,3,4]
"""