from sys import stdin

n, m = map(int,stdin.readline().split())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]
co=0
for i in a:
    if co < min(i):
        co = min(i)
print(co)