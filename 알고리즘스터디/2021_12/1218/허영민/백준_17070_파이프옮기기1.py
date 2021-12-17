def pipe_move(x, y, direction):
    for dir in pipe[direction]:
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:
            if dir != 1:
                result[dir][nx][ny] += result[direction][x][y]
            else:
                if not arr[nx-1][ny] and not arr[nx][ny-1]:
                    result[dir][nx][ny] += result[direction][x][y]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[[0] * N for _ in range(N)] for _ in range(3)]
case = 0
dx = [0, 1, 1]
dy = [1, 1, 0]
pipe = [(0, 1), (0,1,2), (2,1)]
result[0][0][1] = 1
for x in range(N):
    for y in range(N):
        for d in range(3):
            if result[d][x][y] and not arr[x][y]:
                pipe_move(x,y,d)
for i in range(3):
    case += result[i][N-1][N-1]
print(case)