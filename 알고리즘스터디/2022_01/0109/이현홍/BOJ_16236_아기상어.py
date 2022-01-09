N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shark = 2
bait = 0
V = [[0]*N for _ in range(N)]

shark_position = 0
for r in range(N):
    if not shark_position:
        for c in range(N):
            if arr[r][c] == 9:
                shark_position = (r, c, 0)
                arr[r][c] = 0
                V[r][c] = 1
                break

Q = [0] * N * N
front = -1
rear = 0
Q[rear] = shark_position
X = []
distance = 0xfff

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def BFS(r, c, n):
    global distance, rear
    if distance < n: return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and V[nr][nc] == 0:
            if arr[nr][nc] == 0 or arr[nr][nc] == shark:    # 0이나 같은 크기 물고기는 통과
                rear += 1
                Q[rear] = (nr, nc, n+1)
                V[nr][nc] = 1
            elif 0 < arr[nr][nc] < shark:                   # 작은게 있으면 먹이 리스트에 포함
                distance = n+1
                V[nr][nc] = 1
                X.append((n + 1, nr, nc))

t = 0

# 큐
while front != rear:
    X = []
    while front != rear:
        front += 1
        r, c, n = Q[front]
        BFS(r, c, n)
    
    # 큐 범위 내 먹이가 있으면 Q, V 재설정
    if X:
        # 거리, r, c, 순서로 정렬하면 첫번째 요소가 먹이
        X.sort()
        n, r, c = X[0]
        t = n
        shark_position = (r, c, n)
        arr[r][c] = 0

        V = [[0]*N for _ in range(N)]
        V[r][c] = 1

        Q = [0] * N * N
        front = -1
        rear = 0
        Q[rear] = (r, c, n)
        distance = 0xfff

        # 상어 성장
        bait += 1
        if bait == shark:
            shark += 1
            bait = 0

print(t)