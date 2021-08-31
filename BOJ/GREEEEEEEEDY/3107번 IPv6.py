def solution(s):
    if s == '::':
        return '0000:0000:0000:0000:0000:0000:0000:0000'
    s = s.split(':')

    space_cnt = 0
    for i in s:
        if i == '':
            space_cnt += 1
    if space_cnt >= 2:
        index = s.index('')
        del s[index]

    if len(s) < 8:
        cnt = 0
        space_cnt = 0
        for i in s:
            if i != '':
                cnt += 1
        index = s.index('')
        tmp = []
        # 앞부분 추가.
        for i in s[:index]:
            tmp.append(i)
        # ::에서 0 추가.
        for _ in range(8-cnt):
            tmp.append('0')
        # 뒷부분 추가.
        for i in s[(index+1):]:
            tmp.append(i)
        s = tmp.copy()
    ans = []
    for i in s:
        if len(i) != 4:
            ans.append(i.zfill(4))
        else:
            ans.append(i)
    return ':'.join(ans)

if __name__ == '__main__':
    s = input()
    print(solution(s))
"""
25:09::1
"""