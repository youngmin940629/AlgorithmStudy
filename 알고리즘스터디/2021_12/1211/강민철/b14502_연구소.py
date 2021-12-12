import sys;sys.stdin = open('14502.txt')

from collections import deque

def BFS():
    global res
    cnt = 0
    visited = [[0]*M for _ in range(N)]
    tdq = deque()
    di, dj = (1, -1, 0, 0), (0, 0, 1, -1)
    for i in range(len(dq)):
        tdq.append(dq[i])
        visited[dq[i][0]][dq[i][1]] = 2
        cnt += 1
    while tdq:
        i, j = tdq.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] or visited[ni][nj]: continue
            visited[ni][nj] = 2
            tdq.append((ni, nj))
            cnt += 1
            if cnt > res: return
    return cnt

def comb(n, r, s, lev):
    if lev >= r:
        global res
        ans = BFS()
        if ans:
            res = ans
        return
    for i in range(s, n-r+1+lev):
        if arr[i//M][i%M]: continue
        arr[i // M][i % M] = 1
        comb(n, r, i+1, lev+1)
        arr[i // M][i % M] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dq = deque()

res = N*M
bnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            dq.append((i, j))
        elif arr[i][j] == 1:
            bnt += 1

comb(N*M, 3, 0, 0)
print(N*M - res - bnt - 3)