import sys; sys.stdin = open('7568.txt', 'r')
from collections import deque
# 우하좌상 + 층으로 아래 위
dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

# 방문처리 및 날짜 카운팅을 위한 함수 생성
def count_day():
           
    while q:
        h, r, c = q.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and not field[nh][nr][nc] and not visited[nh][nr][nc]:
                
                q.append((nh, nr, nc))
                
                visited[nh][nr][nc] = visited[h][r][c] + 1
                
# 가로, 세로, 높이 입력
M, N, H = map(int, input().split())

# 토마토 입력
field = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]

# 방문처리할 3차원배열
visited = [[[0] * M for _ in range(N)] for i in range(H)]

# 큐 생성
q = deque()

# 토마토가 있고(1) 방문처리 안 됐으면 방문처리 및 큐에 추가
for i in range(H):
    for j in range(N):
        for k in range(M):
            if field[i][j][k] == -1:
                visited[i][j][k] = -1
            elif field[i][j][k] == 1 and not visited[i][j][k]:
                visited[i][j][k] = 1
                q.append((i, j, k))

# 큐 돌면서 방문처리 및 카운팅 진행 위해 함수 실행
count_day()

# 제일 큰 숫자 찾아서 cnt에 저장
cnt = 0
breaker = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if cnt < visited[i][j][k]:
                cnt = visited[i][j][k]
            # visited에 0이 있으면 최종적으로 익지 않은 토마토가 있다는 뜻
            # 반복문 종료
            if not visited[i][j][k]:
                cnt = 0
                breaker = True
                break
        if breaker:
            break
    if breaker:
        break


# 방문처리 할 때 처음 visited[i][j]에 1로 시작했으므로 -1을 해줘야 함
# 시작할 때부터 전부 익어있었다면 visited에 +1이 안 될 것이므로 0이 출력됨
# 익지 않은 토마토가 있으면 -1이 출력됨
print(cnt-1)