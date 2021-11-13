import sys;sys.stdin = open('2580.txt')

arr = [list(map(int, input().split())) for _ in range(9)]

def check(y, x):
    s = set(i for i in range(1,10))
    for i in range(9):
        s.discard(arr[i][x])
    for j in range(9):
        s.discard(arr[y][j])
    ip, jp = y // 3, x // 3
    for i in range(3*ip, 3*ip+3):
        for j in range(3*jp, 3*jp+3):
            s.discard(arr[i][j])
    return tuple(s)

def DFS(n):
    if n >= 81: return 1
    i, j = n // 9, n % 9
    if not arr[i][j]:
        tup = check(i, j)
        for x in tup:
            arr[i][j] = x
            if DFS(n+1): return 1
            arr[i][j] = 0
    else:
        if DFS(n+1): return 1

DFS(0)

for i in range(9):
    print(*arr[i])