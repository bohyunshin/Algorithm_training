def solution(p):
    if p == '':
        return ''
    answer = ''
    count = 0
    correct = True
    for index, s in enumerate(p):
        if s == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            correct = False
        elif count > 0:
            correct = True
        elif count == 0:
            break
    u = p[:index + 1]
    v = p[index + 1:]

    # if u == p and correct:
    #     return u

    if correct:
        v = solution(v)
    else:
        a = ''
        for i in u[1:-1]:
            if i == '(':
                a += ')'
            else:
                a += '('
        u = '(' + a + ')'
        v = solution(v)

    return answer + u + v