# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    names = S.split('; ')
    name2num = {}
    result = ''
    for name in names:
        name_splt = name.split(' ')
        first = name_splt[0].lower()
        last = name_splt[-1]
        # replace possible hyphen
        last = last.replace('-', '').lower()

        address = last + '_' + first

        # check whether same name exists
        try:
            name2num[address] += 1
        except KeyError:
            name2num[address] = 1
        nums = name2num[address]
        address += str(nums) if nums != 1 else ''

        # concatenate compnay name
        address += '@' + C.lower() + '.com'

        result_to_add = name + ' <' + address + '>' + '; '

        result += result_to_add
    return result[:-2]
