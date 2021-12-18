from collections import deque

def bfs():
    global island_num
    while q:
        x, y = q.popleft()
        arr[x][y] = island_num
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] and (nx,ny) not in visited:
                    q.append((nx,ny))
                    visited.append((nx,ny))
    island_num += 1

def bridge(st_land, x, y, dir):
    bridge_distance = 0
    while True:
        x, y = x + dx[dir], y + dy[dir]
        if 0 <= x < N and 0 <= y < M:
            if arr[x][y] == 0:
                bridge_distance += 1
                continue
            elif arr[x][y] == st_land:
                return
            else:
                if bridge_distance >= 2 and island_bridge[st_land][arr[x][y]] > bridge_distance:
                    island_bridge[st_land][arr[x][y]] = island_bridge[arr[x][y]][st_land] = bridge_distance
                return
        else:
            return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
island_num = 1
q = deque()
visited = []
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for x in range(N):
    for y in range(M):
        if arr[x][y] and (x,y) not in visited:
            q.append((x,y))
            visited.append((x,y))
            bfs()
island_bridge = [[0xffffff] * (island_num) for _ in range(island_num)]
for x in range(N):
    for y in range(M):
        if arr[x][y] != 0:
            for direction in range(4):
                bridge(arr[x][y], x, y, direction)
edge = []
for x in range(island_num):
    for y in range(x+1, island_num):
        if island_bridge[x][y] != 0xffffff:
            edge.append((island_bridge[x][y], x, y))
edge.sort()
cnt = 0
p = [i for i in range(island_num)]

def find_set(x):
    while x != p[x]:
        x = find_set(p[x])
    return p[x]

for w, u, v in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        result += w
        p[find_set(v)] = find_set(u)
        if cnt == island_num - 2:
            break
if cnt != island_num -2:
    print(-1)
else:
    print(result)