from sys import stdin

n=int(stdin.readline())
a=[]
for i in range(n):
    a.append(int(stdin.readline()))
    
print(sorted(a, reverse=True))