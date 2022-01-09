from collections import deque

def bfs():
    global move, eat_cnt
    visited = [[0] * N for _ in range(N)]
    eat_fish = []
    check = 0xffffff
    while q:
        x,y,cnt = q.popleft()
        if cnt > check:
            break
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] > shark_size or visited[nx][ny]:
                continue
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != 0 and arr[nx][ny] < shark_size:
                    eat_fish.append((nx,ny,cnt+1))
                    check = cnt
            visited[nx][ny] = 1
            q.append((nx,ny,cnt+1))
    if len(eat_fish) > 0:
        return eat_fish
    return 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
move = 0
eat_cnt = 0
shark_size = 2
shark_x, shark_y = 0, 0
flag = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            arr[x][y] = 0
            shark_x, shark_y = x, y
            flag = 1
            break
    if flag:
        break
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while True:
    q = deque()
    q.append((shark_x,shark_y,0))
    fish = bfs()
    if fish != 0:
        fish.sort()
        x,y,cnt = fish[0]
        move += cnt
        eat_cnt += 1
        arr[x][y] = 0
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
        shark_x, shark_y = x, y
    else:
        break
print(move)