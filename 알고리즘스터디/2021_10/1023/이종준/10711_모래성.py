N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] != '.':
            arr[i][j] = int(arr[i][j])

# 우 우하 하 좌하 좌 좌상 상 우상
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def wave(r, c):
    cnt = 0
    breaker = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '.':
            cnt += 1
    if cnt >= arr[r][c]:
        arr[r][c] = '.'
        breaker += 1
    if breaker:
        return 1
    else:
        return 0


ans = 0

while True:
    tmp = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.':
                tmp += wave(i, j)
    if tmp == 0:
        ans += 1
        break
    ans += 1

print(ans)

# 두번째 케이스부터 오답