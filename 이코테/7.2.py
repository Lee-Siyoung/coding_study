from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

for i in b:
    if i in a:
        print("yes", end=" ")
    else:
        print("no", end=" ")
