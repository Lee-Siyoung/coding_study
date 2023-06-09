from sys import stdin

n, m = map(int,stdin.readline().split())
x, y, direction = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]
d = [[0]* m for _ in range(n)]
d[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction=3
nx,ny = 0,0
count=1
turn_time=0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] ==0 and maps[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if maps[nx][ny] ==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0
        
print(count)