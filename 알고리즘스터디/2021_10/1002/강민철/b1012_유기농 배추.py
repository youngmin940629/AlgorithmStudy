import sys;sys.stdin=open('1012.txt')
# BFS

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1

    visited = [[0]*M for _ in range(N)]
    que = [0] * (N*M)
    F = R = -1
    cnt = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                cnt += 1
                F += 1
                que[F] = [i, j]
                visited[i][j] = cnt
                while F > R:
                    R += 1
                    for d in range(4):
                        ni = que[R][0] + di[d]
                        nj = que[R][1] + dj[d]
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
                            F += 1
                            que[F] = [ni, nj]
                            visited[ni][nj] = cnt
    print(cnt)