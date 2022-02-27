import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visit = [[-1] * M for _ in range(N)]
def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    if visit[x][y] == -1:
        visit[x][y] = 0
        for dir in range(4):
            nx, ny = x + dx[dir] , y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] < arr[x][y]:
                    visit[x][y] += dfs(nx,ny)
    return visit[x][y]

print(dfs(0,0))