a,b = map(int,input().split())
n,m = map(int,input().split())
class robot:
    def __init__(self,x,y,d,num):
        self.x = x
        self.y = y
        self.d = d
        self.num = num
robot_info = []
land = [[[] for _ in range(a)] for _ in range(b)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dct = {'N':0,'E':1,'S':2,'W':3}
for i in range(n):
    y,x,d = input().split()
    x = int(x)
    y = int(y)
    x = b-x
    y -= 1
    d = dct[d]
    r = robot(x,y,d,i)
    robot_info.append(r)
    land[x][y].append(r)
for _ in range(m):
    number,order,cnt = input().split()
    number = int(number)-1
    cnt = int(cnt)
    for _ in range(cnt):
        r = robot_info[number]
        x,y,d = r.x,r.y,r.d
        if order == 'L':
            r.d = (d-1)%4
        elif order == 'R':
            r.d = (d+1)%4
        elif order == 'F':
            nx,ny = x+dx[d],y+dy[d]
            if not (0 <= nx < b and 0 <= ny < a):
                print(f'Robot {number+1} crashes into the wall')
                exit()
            if len(land[nx][ny]) >= 1:
                another_r = land[nx][ny][0]
                print(f'Robot {number + 1} crashes into robot {another_r.num + 1}')
                exit()
            r.x = nx
            r.y = ny
            land[nx][ny].append(r)
            land[x][y].clear()
print('OK')
"""
5 4
2 2
1 1 E
5 4 W
1 F 4
2 F 4
"""