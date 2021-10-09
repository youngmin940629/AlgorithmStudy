# 시간초과, pypy로 하면 통과

import sys; sys.stdin = open('2589.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def func(k, l):
    visited = [[0] * M for _ in range(N)]    
    q.append((k, l))
    visited[k][l] = 1
    
    tmp = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and treasure_map[nr][nc] == 'L':
                    visited[nr][nc] = visited[r][c] + 1
                    # if tmp < visited[nr][nc]:
                    #     tmp = visited[nr][nc]
                    tmp = max(tmp, visited[nr][nc])
                    q.append((nr, nc))
    return tmp - 1



N, M = map(int, input().split())
treasure_map = [list(input()) for _ in range(N)]
q = deque()

ans = 0
for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            ans = max(ans, func(i, j))
print(ans)