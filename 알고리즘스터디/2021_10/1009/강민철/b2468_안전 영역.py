import sys;sys.stdin = open('2468.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
height = set()
for i in range(N):
    height = height.union(arr[i])
height = sorted(list(height))

max_cnt = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for w in height:
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    que = [0] * (N*N)
    F = R = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > w and not visited[i][j]:
                cnt += 1
                visited[i][j] = cnt
                F += 1
                que[F] = [i, j]
                while F > R:
                    R += 1
                    x = que[R][0]
                    y = que[R][1]
                    for d in range(4):
                        ni = x + di[d]
                        nj = y + dj[d]
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > w and not visited[ni][nj]:
                            visited[ni][nj] = cnt
                            F += 1
                            que[F] = [ni, nj]
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)