from itertools import combinations
from collections import deque
n,k = input().split()
m = len(n)
k = int(k)
locs = [i for i in range(m)]
q = deque()
visited = [[-1]*k]