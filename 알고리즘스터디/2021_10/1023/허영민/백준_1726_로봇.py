from collections import deque

def bfs(x,y, dir):
    global result
    visited = [[[0] * N for _ in range(M)] for _ in range(5)]
    visited[dir][x][y] = 1
    while q:
        x,y,dir,cnt = q.popleft()
        if x == end[0] -1 and y == end[1] - 1 and dir == end[2]:
            return cnt
        for i in range(1,4):
            nx = x + i * dx[dir]
            ny = y + i * dy[dir]
            if 0 <= nx < M and 0 <= ny < N and visited[dir][nx][ny]:continue
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    visited[dir][nx][ny] = 1
                    q.append((nx,ny,dir, cnt+1))
                else:
                    break
        for next_dir in range(1,5):
            if dir != next_dir and visited[next_dir][x][y] == 0:
                visited[next_dir][x][y] = 1
                if abs(dir - next_dir) == 1 and not (dir == 2 and next_dir ==3) and not (dir == 3 and next_dir == 2):
                    q.append((x,y,next_dir,cnt+2))
                else:
                    q.append((x,y,next_dir,cnt+1))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
st = list(map(int, input().split()))
end = list(map(int, input().split()))
result = 0
q = deque()
q.append((st[0]-1, st[1]-1, st[2], 0))
print(bfs(st[0]-1, st[1]-1, st[2]))
