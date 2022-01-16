n = int(input())
a = input()
num = []
cal = []
for i in a:
    if i in ['+','-','*']:
        cal.append(i)
    else:
        num.append(int(i))
ans = -1e100
chosen = [0]*len(cal)
def go(index,last):
    global ans
    if index == len(cal):
        num_new = []
        cal_new = []
        for k in range(len(chosen)):
            if chosen[k] == 1:
                if cal[k] == '+':
                    num_new.append(num[k]+num[k+1])
                if cal[k] == '*':
                    num_new.append(num[k]*num[k+1])
                if cal[k] == '-':
                    num_new.append(num[k]-num[k+1])
            else:
                if k == 0:
                    num_new.append(num[k])
                    cal_new.append(cal[k])
                else:
                    if chosen[k-1] == 1:
                        cal_new.append(cal[k])
                    else:
                        num_new.append(num[k])
                        cal_new.append(cal[k])
                    if k == len(chosen)-1:
                        num_new.append(num[k+1])
        tmp = eval(str(num_new[0]) + cal_new[0] + str(num_new[1]))
        for k in range(1,len(cal_new)):
            if cal_new[k] == '*':
                tmp *= num_new[k+1]
            if cal_new[k] == '+':
                tmp += num_new[k+1]
            if cal_new[k] == '-':
                tmp -= num_new[k+1]
        ans = max(ans,tmp)
        return
    if i == len(cal):
        return
    # 괄호 선택.
    if last == -1 or index-last >= 2:
        chosen[index] = 1
        go(index+1,index)
    # 괄호 선택하지 않음.
    chosen[index] = 0
    go(index+1,last)
if n <= 3:
    print(eval(a))
else:
    go(0,-1)
    print(ans)