# 효율 나쁨..
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0
def BFS(r, c, k):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
            global rear
            rear += 1
            visited[nr][nc] = 1
            Q[rear] = (nr, nc, k+1)

Q = [0] * M * N
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            flag = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L'): flag = 1
                # 'L'이 테두리에 있거나 옆에 'W'가 있을 때만 동작
            if flag:
                # visited 초기화
                visited = [[0] * M for _ in range(N)]
                front = -1
                rear = 0
                Q[rear] = (r, c, 1)
                visited[r][c] = 1
                while front != rear:
                    front += 1
                    BFS(Q[front][0], Q[front][1], Q[front][2])
                if Q[rear][2] > answer:
                    answer = Q[rear][2]

# 1로 시작했으므로 -1
print(answer-1)