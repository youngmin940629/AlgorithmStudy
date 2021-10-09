import sys;sys.stdin = open('2583.txt')

M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            arr[i][j] = -1

que = [0] * (M*N)
F = R = -1
cnt = 0
cnt_lst = []

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            cnt += 1
            arr[i][j] = cnt
            F += 1
            que[F] = [i, j]
            area = 1
            while F > R:
                R += 1
                i = que[R][0]
                j = que[R][1]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
                        arr[ni][nj] = cnt
                        F += 1
                        que[F] = [ni, nj]
                        area += 1
            cnt_lst.append(area)

print(cnt)
print(*sorted(cnt_lst))