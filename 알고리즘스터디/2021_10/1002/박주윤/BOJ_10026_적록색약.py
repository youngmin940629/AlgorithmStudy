import sys; sys.stdin = open('BOJ_10026_적록색약.txt', 'r')
sys.setrecursionlimit(10**6)
# N = int(input())
# lst = [input() for _ in range(N)]
# visit = [[0] * N for _ in range(N)]
# visit1 = [[0] * N for _ in range(N)]
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# def sagx(r,c):
#     for k in range(4):
#         visit[r][c] = 1
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == lst[r][c] and visit[nr][nc] == 0:
#             sagx(nr,nc)
#
# def sago(r,c):
#     if lst[r][c] == 'R':
#         for k in range(4):
#             visit1[r][c] = 1
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'R' and visit1[nr][nc] == 0:
#                 sago(nr,nc)
#             elif 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'G' and visit1[nr][nc] == 0:
#                 sago(nr,nc)
#
#     elif lst[r][c] == 'G':
#         for k in range(4):
#             visit1[r][c] = 1
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'R' and visit1[nr][nc] == 0:
#                 sago(nr,nc)
#             elif 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'G' and visit1[nr][nc] == 0:
#                 sago(nr,nc)
#     else:
#         for k in range(4):
#             visit1[r][c] = 1
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == lst[r][c] and visit1[nr][nc] == 0:
#                 sago(nr, nc)
# cnt = 0
# for i in range(N):
#     for j in range(N):
#         if visit[i][j] == 0:
#             sagx(i,j)
#             cnt += 1
# print(cnt, end = ' ')
# cnt1 = 0
# for i in range(N):
#     for j in range(N):
#         if visit1[i][j] == 0:
#             sago(i,j)
#             cnt1 += 1
# print(cnt1)

N = int(input())
# lst = [list(map(str,input().split())) for _ in range(N)]
lst = [list(map(str, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
visit1 = [[0] * N for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def sagx(r,c):
    for k in range(4):
        visit[r][c] = 1
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == lst[r][c] and visit[nr][nc] == 0:
            sagx(nr,nc)
def sago(r,c):
    for k in range(4):
        visit1[r][c] = 1
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == lst[r][c] and visit1[nr][nc] == 0:
            sago(nr,nc)
cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            sagx(i,j)
            cnt += 1
print(cnt, end = ' ')


for i in range(N):
    for j in range(N):
        if lst[i][j] == 'G':
            lst[i][j] = 'R'
cnt1 = 0
for i in range(N):
    for j in range(N):
        if visit1[i][j] == 0:
            sago(i,j)
            cnt1 += 1
print(cnt1)