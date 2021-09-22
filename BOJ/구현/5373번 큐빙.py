garo = [['g','g','g','r','r','r','b','b','b','o','o','o'] for _ in range(3)]
sero = []
for i in range(9):
    if i in [0,1,2]:
        sero.append(['w','w','w'])
    if i in [3,4,5]:
        sero.append(['r','r','r'])
    if i in [6,7,8]:
        sero.append(['y','y','y'])
U = [['w','w','w'] for _ in range(3)]
D = [['y','y','y'] for _ in range(3)]
def move(what,direction):
    if what == 'L':
        if direction == '+':

