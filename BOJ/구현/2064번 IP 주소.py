def to_byte(x):
    x = int(x)
    if x == 0:
        return '0'*8
    result = ''
    while x != 1:
        div,mod = x // 2, x % 2
        result += str(mod)
        x = div
    result += '1'
    return '0'*(8-len(result)) + result[::-1]

def to_num(x):
    result = 0
    i = 0
    for b in x[::-1]:
        if b == '1':
            result += 2**i
        i += 1
    return result
n = int(input())
ip = []
ip_byte = []
for _ in range(n):
    tmp = input().split('.')
    ip.append(list(map(int, tmp)))
    ip_byte.append(''.join(list(map(to_byte, tmp))))

if n == 1:
    print('.'.join(list(map(str,ip[0]))))
    print('255.255.255.255')
    exit()

for i in range(32):

    bit = int(ip_byte[0][i])
    FLAG = True
    for j in range(1,len(ip_byte)):
        if bit ^ int(ip_byte[j][i]) == 1:
            FLAG = False
            m = 32-i
            break
    if FLAG == False:
        break
    else:
        m = 0
mask = '1'*(32-m) + '0'*m
network = ip_byte[0] if m == 0 else ip_byte[0][:-m] + '0'*m
mask_list = []
network_list = []
for i in range(4):
    mask_list.append(to_num(mask[(i*8):(i+1)*8]))
    network_list.append(to_num(network[(i * 8):(i + 1) * 8]))
print('.'.join(list(map(str,network_list))))
print('.'.join(list(map(str,mask_list))))

# TEST CASE
"""
1
10.10.10.10
-> IP가 1개인 경우 네트워크 IP는 걔 자체이고 마스크는 255.255.255.255

2
10.10.10.10
10.10.10.10
-> IP가 모두 같은 경우 네트워크 IP는 걔 자체이고 마스크는 255.255.255.255
"""