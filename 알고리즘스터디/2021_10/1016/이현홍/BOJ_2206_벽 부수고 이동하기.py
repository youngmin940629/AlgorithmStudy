dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS1(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if arr1[nr][nc] == 1 or arr1[nr][nc] > 1-arr1[r][c]: arr1[nr][nc] = -arr1[r][c] + 1
            elif arr1[nr][nc] == 0 or arr1[nr][nc] < arr1[r][c] - 1:
                arr1[nr][nc] = arr1[r][c] -1
                global r1
                r1 += 1
                Q1[r1] = (nr, nc)

def BFS2(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if arr2[nr][nc] == 1 or arr2[nr][nc] > 1-arr2[r][c]: arr2[nr][nc] = -arr2[r][c] + 1
            elif arr2[nr][nc] == 0 or arr2[nr][nc] < arr2[r][c] - 1:
                arr2[nr][nc] = arr2[r][c] -1
                global r2
                r2 += 1
                Q2[r2] = (nr, nc)

N, M = map(int, input().split())
arr1 = [list(map(int, (":".join(input())).split(":"))) for _ in range(N)]
arr2 = arr1[0]* N
for i in range(N):
    arr2[i] = arr1[i][:]
answer = -1

Q1 = [0] * N * M
Q2 = [0] * N * M
f1 = f2 = r1 = r2 = -1

arr1[0][0] = -1
r1 += 1
Q1[r1] = (0, 0)
while f1 != r1:
    f1 += 1
    BFS1(Q1[f1][0], Q1[f1][1])

arr2[N-1][M-1] = -1
r2 += 1
Q2[r2] = (N-1, M-1)
while f2 != r2:
    f2 += 1
    BFS2(Q2[f2][0], Q2[f2][1])

if arr1[N-1][M-1] != 0: answer = -arr1[N-1][M-1]

for r in range(N):
    for c in range(M):
        if arr1[r][c] > 1 and arr2[r][c] > 1:
            tmp = arr1[r][c] + arr2[r][c] - 1
            if answer == -1 or answer > tmp: answer = tmp

if N == 1 and M == 1:
    answer = 1

print(answer)