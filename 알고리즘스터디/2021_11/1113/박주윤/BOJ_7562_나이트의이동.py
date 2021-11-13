import sys; sys.stdin = open('BOJ_7562_나이트의이동.txt', 'r')
from collections import deque

dx = [2,2,1,-1,-2,-2,-1,1]
dy = [1,-1,-2,-2,-1,1,2,2]

def bfs():
    global ans
    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            if ans > cnt:
                ans = cnt
                return
        else:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt+1))



for tc in range(1, int(input())+1):
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    ans = N ** 2

    q = deque()
    q.append((sx, sy, 0))
    bfs()
    print(ans)