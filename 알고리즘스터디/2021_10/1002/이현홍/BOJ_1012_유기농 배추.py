import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c, num):
    arr[r][c] = num
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0<= nr < N and 0 <= nc < M:
            if arr[nr][nc] == -1:
                BFS(nr, nc, num)

T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0]* M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = -1
    num = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == -1:
                num += 1
                BFS(r, c, num)
    print(num)