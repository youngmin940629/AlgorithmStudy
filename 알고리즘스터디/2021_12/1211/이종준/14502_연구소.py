# python3 시간초과, pypy3 1400ms
from collections import deque

N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 최종 정답
ans = 0
        
# 바이러스 퍼뜨리면서 안전지대 최대값 찾기
def bfs():
    global ans
    tmp_map = [[0] * M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            tmp_map[i][j] = my_map[i][j]
            if tmp_map[i][j] == 2:
                q.append((i, j))
            
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if tmp_map[nr][nc] == 0:
                    tmp_map[nr][nc] = 2
                    q.append((nr, nc))

    tmp = 0
    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 0:
                tmp += 1
    if tmp > ans:
        ans = tmp

# 시간 오래 걸릴거같긴 하지만...벽 3개 세우기(완탐으로)
def wall(cnt):
    if cnt == 3:
        bfs()
        return    
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 0:
                my_map[i][j] = 1
                wall(cnt + 1)
                my_map[i][j] = 0

wall(0)
print(ans)