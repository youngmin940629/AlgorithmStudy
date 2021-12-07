from collections import deque

def bfs():
    visited = [arr[i][:] for i in range(N)]
    cnt = 0
    for v in virus:
        q.append(v)
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    visited[nx][ny] = 2
                    q.append((nx,ny))
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(map(int ,input(). split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
virus = []
blank = []
q = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 2:
            virus.append((x,y))
        elif arr[x][y] == 0:
            blank.append((x,y))

for a in range(len(blank)):
    for b in range(a+1, len(blank)):
        for c in range(b+1, len(blank)):
            arr[blank[a][0]][blank[a][1]] = arr[blank[b][0]][blank[b][1]] = arr[blank[c][0]][blank[c][1]] = 1
            result = max(result, bfs())
            arr[blank[a][0]][blank[a][1]] = arr[blank[b][0]][blank[b][1]] = arr[blank[c][0]][blank[c][1]] = 0
print(result)