s = input()

int_list = []
str_list = []
for i in s:
    try:
        i = int(i)
    except:
        pass
    if isinstance(i, str):
        str_list.append(i)
    else:
        int_list.append(int(i))
print(''.join(sorted(str_list)) + str(sum(int_list)))