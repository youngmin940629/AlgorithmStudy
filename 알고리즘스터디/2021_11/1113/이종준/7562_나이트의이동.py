from collections import deque

# 나이트가 움직이는 방향
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    global ans
    while q:
        r, c, cnt = q.popleft()
        if arr[r][c] == 2:
            return cnt

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1                
                q.append((nr, nc, cnt + 1))
                


result = []

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    r, c = map(int, input().split())
    er, ec = map(int, input().split())
    
    arr[r][c] = 1
    arr[er][ec] = 2

    visited = [[0] * N for _ in range(N)]

    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1


    result.append(bfs())

for res in result:
    print(res)