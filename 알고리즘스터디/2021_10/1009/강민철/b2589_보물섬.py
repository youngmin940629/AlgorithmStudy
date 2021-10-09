import sys;sys.stdin = open('2589.txt')


N, M = map(int, input().split())
arr = [input() for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0]*M for _ in range(N)]
            que = [0] * (N*M)
            F = R = -1
            visited[i][j] = 1
            F += 1
            que[F] = [i, j]
            while F > R:
                R += 1
                x, y = que[R][0], que[R][1]
                for d in range(4):
                    ni = x + di[d]
                    nj = y + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 'L':
                        visited[ni][nj] = visited[x][y] + 1
                        F += 1
                        que[F] = [ni, nj]
                        if visited[ni][nj] > res:
                            res = visited[ni][nj]

print(res-1)
