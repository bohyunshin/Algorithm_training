def solution(s):
    n = len(s)
    max_split = n // 2
    result = []

    for j in range(1, max_split + 1):
        comp_s = ''
        count = 1
        previous = s[0:j]
        m = len(s) // j
        for i in range(n - 1):

            if s[i * j:(i + 1) * j] == s[(i + 1) * j:(i + 2) * j]:
                count += 1
                if i == len(s) - 2:
                    comp_s += str(count) + previous
            else:
                comp_s += (str(count) if count != 1 else '') + previous
                count = 1
                previous = s[(i + 1) * j:(i + 2) * j]
                if i == len(s) - 2:
                    comp_s += (str(count) if count != 1 else '') + previous
            comp_s = comp_s.strip()

        try:
            int(comp_s[-1])
            try:
                int(comp_s[-2])
                comp_s = comp_s[:-2]
            except:
                comp_s = comp_s[:-1]
        except:
            pass
        result.append(len(comp_s))
    return min(result)