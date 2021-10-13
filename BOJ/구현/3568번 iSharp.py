from string import ascii_lowercase, ascii_uppercase
str_splt = input().split()
for i,s in enumerate(str_splt):
    base = str_splt[0]
    if i == 0:
        continue
    s = s[:-1]
    var = ''
    pointer = ''
    for j in s:
        if j in ascii_lowercase + ascii_uppercase:
            var += j
        else:
            pointer += j
    # print(pointer,var,base)
    for j in pointer[::-1]:
        if j == '[':
            base += ']'
        elif j == ']':
            base += '['
        else:
            base += j
    print(base,var+';')