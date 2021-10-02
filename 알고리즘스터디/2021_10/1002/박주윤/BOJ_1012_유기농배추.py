import sys; sys.stdin = open('BOJ_1012_유기농배추.txt', 'r')
import sys
sys.setrecursionlimit(10**6)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(r,c):
    for k in range(4):
        visit[r][c] = 1
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 1 and visit[nr][nc] == 0:
            dfs(nr,nc)
for tc in range(1, int(input())+1):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    s = []
    for _ in range(K):
        x,y = map(int, input().split())
        lst[y][x] += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
