from sys import stdin
n, m, k = map(int, stdin.readline().split())

a = sorted(list(map(int, stdin.readline().split())), reverse=True)
count=0
cu = 0
for i in range(m):
    if cu == k:
        count+=a[1]
        cu=0
        continue
    count+=a[0]
    cu+=1
print(count)