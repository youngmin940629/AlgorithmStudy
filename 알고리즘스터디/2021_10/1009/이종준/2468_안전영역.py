import sys; sys.stdin = open('2468.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def func():
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and data[nr][nc] > rain and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 1

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 구하기
max_height = 0
for i in range(N):
    for j in range(N):
        if data[i][j] > max_height:
            max_height = data[i][j]

rain = 0
max_area = 0

while rain <= max_height:
    tmp_area = 0
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] > rain and not visited[i][j]:
                visited[i][j] = 1
                q.append((i, j))
                tmp_area += func()
    if tmp_area > max_area:
        max_area = tmp_area
    rain += 1
print(max_area)