k = int(input())
boodeungho = input().split()
min_list = [i for i in range(10)]
max_list = min_list[::-1]

continuous = []
start = 1
for i in range(len(boodeungho)):
    if i == len(boodeungho)-1:
        break
    if boodeungho[i] == boodeungho[i+1]:
        start += 1
    else:
        continuous.append(str(start) + '.' + boodeungho[i])
        start = 1
if boodeungho[i] == boodeungho[i-1]:
    continuous.append(str(start) + '.' + boodeungho[i])
else:
    # continuous.append(str(start) + boodeungho[i-1])
    continuous.append(str(1) + '.' + boodeungho[i])

answer_max = '9' if boodeungho[0] == '>' else '8'
answer_min = '1' if boodeungho[0] == '>' else '0'
lst_max = [i for i in range(10) if i != int(answer_max)]
lst_min = [i for i in range(10) if i != int(answer_min)]

for i in continuous:
    num, boo = int(i.split('.')[0]), i.split('.')[1]

    if boo == '<':
        max_index = lst_max.index(max(lst_max))
        if num == 1:
            answer_max += str(max(lst_max))
            lst_max.pop(max_index)
        else:
            to_add = lst_max[max_index-num:max_index]

    # answer += lst[index:index+num]
