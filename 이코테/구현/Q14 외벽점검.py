from itertools import permutations


def solution(n, weak, dist):
    for i in weak:
        if i >= n:
            return 1
    answer = 0
    total = len(weak)
    weak += [i + n for i in weak]
    min_friend = 1e10
    for start in weak:
        for p in permutations(dist):
            current = start
            num_freind = 0

            for d in p:
                current += d
                num_freind += 1
                fixed = 0

                for i in weak:
                    if start <= i <= current:
                        fixed += 1
                    if i > current:
                        current = i
                        break

                if fixed >= total:
                    if min_friend > num_freind:
                        min_friend = num_freind
                    break
    if min_friend == 1e10:
        return -1
    else:
        return min_friend