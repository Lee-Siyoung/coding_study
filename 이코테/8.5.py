from sys import stdin

n,m=map(int,stdin.readline().split())
a=[]
for i in n:
    a.append(int(stdin.readline()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(a[i],m+1):
        d[j]=min(d[j],d[j-a[i]]+1)
        
if d[m]==10001:
    print(-1)
else:
    print(d[m])
    
