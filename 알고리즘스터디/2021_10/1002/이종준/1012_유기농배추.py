# 영민이 답 참고해서 deque과 bfs방식 사용해서 해결함

import sys; sys.stdin = open('1012.txt', 'r')
from collections import deque

T = int(input())

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def worm(r, c):
    global visited
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 1


for _ in range(T):
    M, N, E = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    for _ in range(E):
        s, e = map(int, input().split())
        field[e][s] = 1

    result = 0

    q = deque()

    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                q.append((i, j))
                result += worm(i, j)

    print(result)

    