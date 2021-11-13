def bishop(idx,cnt,check_color):
    global w_rst, b_rst
    if check_color == 0:
        if N * N - idx + 1 + cnt <= w_rst or idx >= N * N:
            return
        w_rst = max(w_rst,cnt)
    elif check_color == 1:
        if N * N - idx + 1 + cnt <= b_rst or idx >= N * N:
            return
        b_rst = max(b_rst,cnt)
    x, y = idx // N , idx % N
    for i in range(x,N):
        while y < N:
            next_idx = i * N + y
            if not visit[next_idx] and chess[i][y] == 1 and check(i,y):
                visit[next_idx] = 1
                bishop(next_idx, cnt+1, check_color)
                visit[next_idx] = 0
            y += 2
        if i % 2:
            y = check_color
        else:
            y = (check_color + 1) % 2


def check(x,y):
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        while 0 <= nx < N and 0 <= ny < N:
            if not visit[nx * N + ny]:
                nx += dx[dir]
                ny += dy[dir]
            else:
                return False
    return True

N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * (N*N)
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]
w_rst = b_rst = 0
bishop(0, 0, 0)
bishop(1, 0, 1)
print(w_rst + b_rst)