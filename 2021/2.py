from math import sqrt


def check(prime, front, back):
    if '0' in prime:
        return False
    if front != '' and back != '':
        if front == '0' and back == '0':
            return True
        else:
            return False
    elif front == '' and back != '':
        if back == '0':
            return True
        else:
            return False
    elif front != '' and back == '':
        if front == '0':
            return True
        else:
            return False
    elif front == '' and back == '':
        return True


def N_digit(number, base):
    notation = '0123456789'
    q, r = divmod(number, base)
    n = notation[r]
    return N_digit(q, base) + n if q else n


def solution(n, k):
    answer = -1
    # 최대 len(str(n_digit)) -> 20자리
    # Brute Force로 1자리,2자리 다 찾아봐도 될듯?
    n_digit = str(N_digit(n, k))
    # 소수 먼저 찾아 두기
    n = 1000000
    array = [True for i in range(n + 1)]
    for i in range(2, int(sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    LEN = len(n_digit)
    prime = []
    for i in range(1, LEN + 1):
        start = 0
        end = start + i
        while end <= LEN:
            tmp = n_digit[start:end]
            print(tmp)
            if tmp[0] != '0' and array[int(tmp)]:
                print(start,end)
                if start == 0:
                    front = ''
                else:
                    front = n_digit[start - 1]
                if end >= LEN-1:
                    end = ''
                else:
                    end = n_digit[end + 1]
                if check(tmp, front, end):
                    prime.append(tmp)
            start += 1
            end = start + i
    print(prime)

n = 437674
k = 3
solution(n,k)