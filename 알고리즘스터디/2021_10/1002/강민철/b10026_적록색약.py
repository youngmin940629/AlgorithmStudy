import sys;sys.stdin = open('10026.txt')

N = int(input())
arr = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnta = 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
que = [0] * (N**2)
F = R = -1

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnta += 1
            F += 1
            que[F] = [i, j]
            visited[que[F][0]][que[F][1]] = cnta
            while F > R:
                R += 1
                for d in range(4):
                    ni = que[R][0] + di[d]
                    nj = que[R][1] + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[que[R][0]][que[R][1]] == arr[ni][nj]:
                        F += 1
                        que[F] = [ni, nj]
                        visited[que[F][0]][que[F][1]] = cnta

visited = [[0]*N for _ in range(N)]
que = [0] * (N**2)
F = R = -1
cntb = 0

for i in range(N):
    arr[i] = arr[i].replace('R', 'G')

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cntb += 1
            F += 1
            que[F] = [i, j]
            visited[que[F][0]][que[F][1]] = cntb
            while F > R:
                R += 1
                for d in range(4):
                    ni = que[R][0] + di[d]
                    nj = que[R][1] + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[que[R][0]][que[R][1]] == arr[ni][nj]:
                        F += 1
                        que[F] = [ni, nj]
                        visited[que[F][0]][que[F][1]] = cntb

print(cnta, cntb)