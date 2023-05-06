from sys import stdin

n, k = map(int, stdin.readline().split())
a=sorted(list(map(int, stdin.readline().split())))
b=sorted(list(map(int, stdin.readline().split())), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))
