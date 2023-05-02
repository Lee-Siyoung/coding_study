from sys import stdin

n = int(stdin.readline())
a = list(map(str, stdin.readline().split()))
x, y = 1, 1
nx,ny=0,0
for i in a:
    if i == 'R':
        ny =y+1
    elif i == 'L':
        ny = y-1
    elif i == 'U':
        nx = x-1
    elif i == 'D':
        nx= x+1
    if nx<1 or ny <1 or nx>n or ny>n:
        continue
    x, y = nx, ny
print(x, y)