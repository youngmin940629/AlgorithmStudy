import sys;sys.stdin = open('16236.txt')

from collections import deque

def BFS():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                pos = (i, j)

    size = 2
    ate = 0
    t = 0

    dq = deque()
    di = (1, -1, 0, 0)
    dj = (0, 0, 1, -1)

    visited = [[0] * N for _ in range(N)]
    visited[pos[0]][pos[1]] = 1
    arr[pos[0]][pos[1]] = 0
    dq.append(pos)
    tt = 0
    while dq:
        tg = 7 # 물고기 크기 최대 6
        ty = tx = 20
        for _ in range(len(dq)):
            i, j = dq.popleft()
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj] or arr[ni][nj] > size: continue
                dq.append((ni, nj))
                visited[ni][nj] = 1
                if 0 < arr[ni][nj] < size:
                    if ni > ty: continue
                    if ni == ty and nj > tx: continue
                    tg = arr[ni][nj]
                    ty, tx = ni, nj
        t += 1
        if tg < 7:
            ate += 1
            arr[ty][tx] = 0
            visited = [[0] * N for _ in range(N)]
            dq = deque()
            dq.append((ty, tx))
            if ate >= size:
                size += 1
                ate = 0
            tt += t
            t = 0
    return tt

print(BFS())