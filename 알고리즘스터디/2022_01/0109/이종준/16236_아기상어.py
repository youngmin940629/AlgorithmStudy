from collections import deque

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 이동에 걸린 시간(초)
ans = 0

# 상어 크기
shark_size = 2

# 먹은 물고기 수
fish = 0

# 상어 위치 찾기
shark_r = 0
shark_c = 0

breaker = False
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            data[i][j] = 0
            breaker = True
            shark_r = i
            shark_c = j
            break
    if breaker:
        break

while True:
    q = deque()
    q.append((shark_r, shark_c, 0))
    visited = [[0] * N for _ in range(N)]
    breaking = 987654321
    hunt = []
    while q:
        r, c, cnt = q.popleft()
        # 먹을 거 찾았으면 break
        if cnt > breaking:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 벽 만나거나 방문했으면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            # 상어보다 덩치가 큰 물고기 패스
            if data[nr][nc] > shark_size or visited[nr][nc]: continue
            # 먹을 게 있으면 hunt에 저장
            if data[nr][nc] and data[nr][nc] < shark_size:
                hunt.append((nr, nc, cnt + 1))
                breaking = cnt
            # 방문처리하고 이동
            visited[nr][nc] = 1
            q.append((nr, nc, cnt + 1))

    # 먹을 게 있다면
    if len(hunt) > 0:
        # 가장 위, 가장 왼쪽부터 먹으므로 오름차순 정렬
        hunt.sort()
        r, c, tmp_ans = hunt[0][0], hunt[0][1], hunt[0][2]
        # 이동시간 늘리기
        ans += tmp_ans
        
        # 먹었으면 0으로 만들어주기
        data[r][c] = 0

        # 먹은 개수 늘리면서 크기 늘릴지 여부 비교
        fish += 1
        if shark_size == fish:
            shark_size += 1
            fish = 0
        # 먹은 자리로 상어 이동시키기
        shark_r = r
        shark_c = c
    # 먹을 게 없으면 끝내고 정답 출력!
    else:
        break

print(ans)