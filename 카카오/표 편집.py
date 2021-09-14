from bisect import bisect_left, bisect_right, bisect


def solution(n, k, cmd):
    answer = ''
    table = [i for i in range(n)]
    count = [1] * n
    del_hist_dct = {}
    del_hist_s = []
    stack = []
    next_k = {i:i+1 for i in range(n)}
    next_k[n-1] = n-2
    del_cnt = 0
    z_cnt = 0
    for c in cmd:
        # 이분 탐색을 위해 sorting 해둠.
        del_hist_s.sort()
        m = len(del_hist_s)
        if c[0] in ['U', 'D']:
            d, cnt = c.split()
            cnt = int(cnt)
            if d == 'U':
                lower = k - cnt
                upper = k
                k = k - cnt - (bisect_right(del_hist_s, upper, 0, m) - bisect_left(del_hist_s, lower, 0, m))
            else:
                lower = k
                upper = k + cnt
                k = k + cnt + (bisect_right(del_hist_s, upper, 0, m) - bisect_left(del_hist_s, lower, 0, m))
        elif c == 'C':
            del_hist_dct[del_cnt] = k
            del_hist_s.append(k)
            stack.append(k)
            count[k] -= 1
            while count[k] == 0:
                k += 1
                if k >= n:
                    break
            if k == n:
                k -= 1
                while count[k] == 0:
                    k -= 1
        elif c == 'Z':
            z_cnt += 1
            z = stack[-z_cnt]
            if k >= z:
                k += 1
            count[z] += 1
            z_index = bisect(del_hist_s,z,0,m)
            del_hist_s[z_index-1] = -1
    print(count,k)
n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z","U 1", "C"]
solution(n,k,cmd)

# a = [1,2,7]
# print(bisect(a,7,0,3))