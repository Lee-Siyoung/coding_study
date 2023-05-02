from sys import stdin

n = (stdin.readline())
ahp = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x, y= ahp[n[0]], int(n[1])
a = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
co=0
for i in a:
    nx, ny=x,y
    nx += i[0]
    ny += i[1]
    if nx<1 or ny<1 or nx>9 or nx>9:
        continue
    
    co +=1
print(co)