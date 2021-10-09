import sys; sys.stdin = open('2636.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def func():
    q= deque()
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q.append((0, 0))
    cnt = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                elif board[nr][nc] == 1:
                    visited[nr][nc] = 1
                    board[nr][nc] = 0
                    cnt += 1
    cnt_list.append(cnt)
    return cnt
    


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt_list = []
hour = 0

while True:
    tmp = func()
    if tmp == 0:
        break
    hour += 1
print(hour)
print(cnt_list[-2])