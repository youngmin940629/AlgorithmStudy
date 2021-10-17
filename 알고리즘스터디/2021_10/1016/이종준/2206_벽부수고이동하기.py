import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q= deque()
    visited = [[[0] * M for _ in range(N)] for __ in range(2)]
    visited[1][0][0] = 1
    q.append((1, 0, 0)) # 벽부수기 가능횟수, r, c

    while q:
        chance, r, c = q.popleft()

        if r == N - 1 and c == M - 1:
            return visited[chance][N-1][M-1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and chance == 1:
                    visited[0][nr][nc] = visited[1][r][c] + 1
                    q.append((0, nr, nc))

                elif arr[nr][nc] == 0 and not visited[chance][nr][nc]:
                    visited[chance][nr][nc] = visited[chance][r][c] + 1
                    q.append((chance, nr, nc))

    return -1



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

print(bfs())