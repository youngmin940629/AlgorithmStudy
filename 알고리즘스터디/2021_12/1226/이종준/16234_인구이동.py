# python3 시간초과 / pypy3 1212ms

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def border(r, c):
    global data, is_moved
    population = data[r][c]
    country_cnt = 1
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    united = [(r, c)]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(data[r][c] - data[nr][nc]) <= R:
                visited[nr][nc] = 1
                q.append((nr, nc))
                united.append((nr, nc))
                country_cnt += 1
                population += data[nr][nc]
    tmp_division = population // country_cnt
    if country_cnt >= 2:
        is_moved = True
        for country in united:
            i, j = country
            data[i][j] = tmp_division

    
cnt = 0
while True:
    is_moved = False
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                border(r, c)
    if is_moved:
        cnt += 1
    else:
        break

print(cnt)