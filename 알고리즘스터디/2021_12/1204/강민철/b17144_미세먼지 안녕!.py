import sys;sys.stdin = open('17144.txt')

from collections import deque

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

puri = []
dust = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            dust.append([arr[i][j], i, j])
        elif arr[i][j] < 0:
            puri.append(i)

di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

while T > 0:
    T -= 1
    while dust:
        d, i, j = dust.popleft()
        m = d // 5
        for _ in range(4):
            ni, nj = i + di[_], j + dj[_]
            if ni < 0 or ni >= R or nj < 0 or nj >= C or arr[ni][nj] < 0: continue
            arr[ni][nj] += m
            arr[i][j] -= m

    for i in range(puri[0], 0, -1):
        if i == puri[0]:
            arr[i-1][0] = 0
        arr[i][0] = arr[i-1][0]
        arr[i-1][0] = 0
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
        arr[0][j+1] = 0
    for i in range(puri[0]):
        arr[i][C-1] = arr[i+1][C-1]
        arr[i+1][C-1] = 0
    for j in range(C-1, 1, -1):
        arr[puri[0]][j] = arr[puri[0]][j-1]
        arr[puri[0]][j-1] = 0

    for i in range(puri[1], R-1):
        if i == puri[1]:
            arr[i+1][0] = 0
        arr[i][0] = arr[i+1][0]
        arr[i+1][0] = 0
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
        arr[R-1][j+1] = 0
    for i in range(R-1, puri[1], -1):
        arr[i][C-1] = arr[i-1][C-1]
        arr[i-1][C-1] = 0
    for j in range(C-1, 1, -1):
        arr[puri[1]][j] = arr[puri[1]][j-1]
        arr[puri[1]][j-1] = 0

    if T > 0:
        for i in range(R):
            for j in range(C):
                if arr[i][j] > 0:
                    dust.append([arr[i][j], i, j])

res = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            res += arr[i][j]

print(res)