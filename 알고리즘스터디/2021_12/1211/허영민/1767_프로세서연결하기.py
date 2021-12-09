def dfs(n, m, cnt):
    global core_num, result
    if core_num < sum(n):
        core_num = sum(n)
        result = 0xffffff
    if core_num == sum(n):
        if result > cnt:
            result = cnt
    for i in range(m, len(core)):
        x, y = core[i][0], core[i][1]
        for dir in range(4):
            wire_num = wire(x,y,dir)
            if wire_num:
                now = n[:]
                now[i] = 1
                dfs(now, i+1, cnt+wire_num)
                nx, ny = x, y
                for _ in range(wire_num):
                    nx, ny = nx + dx[dir], ny + dy[dir]
                    process[nx][ny] = 0



def wire(x,y,dir):
    wire_cnt = 0
    flag = 0
    while 0 < x < N-1 and 0 < y < N-1:
        x += dx[dir]
        y += dy[dir]
        if process[x][y] == 0:
            wire_cnt += 1
            process[x][y] = 1
        elif process[x][y] == 1:
            flag = 1
            break
    if flag == 1:
        for i in range(wire_cnt):
            x -= dx[dir]
            y -= dy[dir]
            process[x][y] = 0
        return 0
    elif flag == 0:
        return wire_cnt


for tc in range(int(input())):
    N = int(input())
    process = [list(map(int, input().split())) for _ in range(N)]
    core = []
    for x in range(N):
        for y in range(N):
            if process[x][y] == 1 and x !=0 and x != N-1 and y != 0 and y != N-1:
                core.append((x,y))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [0] * len(core)
    core_num = 0
    result = 0xffffff
    dfs(visited, 0, 0)
    print('#{} {}'.format(tc+1, result))