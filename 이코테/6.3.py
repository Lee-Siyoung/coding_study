from sys import stdin

n=int(stdin.readline())
a=[]
for i in range(n):
    a.append(list(map(str, stdin.readline().split())))
a=sorted(a, key=lambda x : x[1])
for i in a:
    print(i[0], end=" ")