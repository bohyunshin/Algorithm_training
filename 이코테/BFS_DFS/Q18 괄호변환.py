def is_correct_parenth(p):
    a = 0
    for i in p:
        if i == '(':
            a += 1
        else:
            a -= 1
        if a < 0:
            return False
    return True


def is_balanced_parenth(p):
    a = 0
    for i in p:
        if i == '(':
            a += 1
        else:
            a -= 1
    if a == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    if p == '' or is_correct_parenth(p):
        return p
    # answer = ''
    for index in range(1, len(p) + 1):
        u = p[:index]
        v = p[index:]
        if is_balanced_parenth(u) and is_balanced_parenth(v):
            break

    # print(u,len(u))
    # print(v,len(v))
    if is_correct_parenth(u):
        v = solution(v)
        # return u+v
        answer = u + v
    else:
        v = '(' + solution(v) + ')'
        tmp = ''
        u = u[1:-1]
        for i in u:
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
        u = tmp
        # return v+u
        answer = v + u
    return answer