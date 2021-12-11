virus = []
v_side = []
safe = 0

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for r in range(R):
    for c in range(C):
        if arr[r][c] == 2:
            virus.append((r, c))
        elif arr[r][c] == 0:
            v_side.append((r, c))
            safe += 1

V = [0] * len(v_side)
V2 = [[0]*C for _ in range(R)]

result = 0
cnt = 0
Q, front, rear = virus[:] + [0]*100, -1, len(virus)-1

#바이러스 확산
def diffusion():
    global front, rear, cnt
    while front != rear:
        front += 1
        r, c = Q[front]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0 and V2[nr][nc] == 0:
                rear += 1
                Q[rear] = (nr, nc)
                cnt += 1
                V2[nr][nc] = 1

# 벽 놓을 곳 완전 탐색
def sc(n=0, s=0):
    if s > 3: return
    if n == len(v_side):
        if s == 3:
            global V2, cnt, result, Q, front, rear
            V2 = [[0]*C for _ in range(R)]
            cnt = 0
            Q, front, rear = virus[:] + [0]*100, -1, len(virus)-1
            diffusion()
            area = safe - cnt
            if result < area:
                result = area
    else:
        sc(n+1, s)
        V[n] = 1
        r, c = v_side[n]
        arr[r][c] = 1
        sc(n+1, s+1)
        V[n] = 0
        arr[r][c] = 0

sc()
# 벽 3개 빼기
print(result-3)