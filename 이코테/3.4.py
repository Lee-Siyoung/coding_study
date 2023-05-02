from sys import stdin

n, k = map(int,stdin.readline().split())
co=0
while(n != 1):
    if n%k==0:
        co+=1
        n = n//k
    else:
        n = n - 1
        co+=1
print(co)