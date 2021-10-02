import sys; sys.stdin = open('BOJ_2667_단지번호붙이기.txt', 'r')
N = int(input())
lst = [input() for _ in range(N)]
visit = [[0] * N for _ in range(N)]

dang = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = 1
def dfs(r, c):
    global cnt
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        visit[r][c] = 1
        if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == '1' and visit[nr][nc] == 0:
            cnt += 1
            dfs(nr, nc)

s = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == '1' and visit[i][j] == 0:
            cnt = 1
            dfs(i, j)
            s.append(cnt)
            dang += 1
print(dang)
for i in sorted(s):
    print(i)