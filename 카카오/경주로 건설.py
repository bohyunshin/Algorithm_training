def solution(s):
    start = 0
    end = 0
    n = len(s)
    answer = ''
    num_list = [str(i) for i in range(0,10)]
    string2num = {}
    string2num['zero'] = 0
    string2num['one'] = 1
    string2num['two'] = 2
    string2num['three'] = 3
    string2num['four'] = 4
    string2num['five'] = 5
    string2num['six'] = 6
    string2num['seven'] = 7
    string2num['eight'] = 8
    string2num['nine'] = 9

    while start < n-1 or end < n-1:
        if s[end] in num_list:
            answer += str(s[end])
            start += 1
            end += 1
        elif s[start:end+1] in string2num.keys():
            answer += str( string2num[s[start:end+1]] )
            start = end+1
            end += 1
        elif s[end+1] in num_list:
            answer += s[start:end+1]
            start = end+1
            end += 1
        else:
            end += 1
    print(start,end,len(s))
    if start == end and start == len(s):
        return int(answer)
    else:
        if s[start:end+1] in num_list:
            answer += s[start:end+1]
        else:
            answer += string2num[s[start:end+1]]
        return int(answer)

# print(solution('one4seveneight'))
print(solution('23four5six7'))