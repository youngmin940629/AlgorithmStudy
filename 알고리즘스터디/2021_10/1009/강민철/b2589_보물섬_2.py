import sys;sys.stdin = open('2589.txt')

from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def solve():
    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                visited = [[0]*M for _ in range(N)]
                dq = deque()
                visited[i][j] = 1
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for d in range(4):
                        ni = x + di[d]
                        nj = y + dj[d]
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 'L':
                            visited[ni][nj] = visited[x][y] + 1
                            dq.append((ni, nj))
                            if visited[ni][nj] > res:
                                res = visited[ni][nj]
    return res

print(solve()-1)