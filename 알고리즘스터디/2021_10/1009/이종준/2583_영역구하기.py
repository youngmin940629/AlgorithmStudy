import sys; sys.stdin = open('2583.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def func():
    global area_list
    count = 0
    while Q:
        count += 1
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not my_map[nr][nc] and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = 1
    area_list.append(count)
    return 1



M, N, K = map(int, input().split())
rectangle_points = [list(map(int, input().split())) for _ in range(K)]

Q = deque()

my_map = [[0] * M for _ in range(N)]

for idx in rectangle_points:
    for i in range(idx[0], idx[2]):
        for j in range(idx[1], idx[3]):
            my_map[i][j] = 1

visited = [[0] * M for _ in range(N)]

area_list = []
cnt = 0

for i in range(N):
    for j in range(M):
        if my_map[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            Q.append((i, j))
            cnt += func()
print(cnt)
area_list.sort()
print(' '.join(map(str, area_list)))