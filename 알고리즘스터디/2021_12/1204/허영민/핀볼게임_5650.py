def pinbole(x,y,dir):
    cnt = 0
    st_x, st_y = x, y
    while True:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x < N and 0 <= y < N:
            if (x == st_x and y == st_y) or arr[x][y] == -1:
                return cnt
            if 1 <= arr[x][y] <= 5:
                dir = change_block[arr[x][y]][dir]
                cnt += 1
            elif 6 <= arr[x][y] <= 10:
                worm_hole = wormhole[arr[x][y]]
                for hole_x,hole_y in worm_hole:
                    if (x,y) != (hole_x,hole_y):
                        x, y = hole_x, hole_y
                        break
        else:
            dir = change_block[5][dir]
            cnt += 1

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0]*N for _ in range(N)]
    st = []
    result = 0
    change_block = [(),
                    (2,0,3,1),
                    (2,3,1,0),
                    (1,3,0,2),
                    (3,2,0,1),
                    (2,3,0,1)]
    wormhole = {
        6 : [],
        7 : [],
        8 : [],
        9 : [],
        10 : [],
    }
    for x in range(N):
        for y in range(N):
            if 6 <= arr[x][y] <= 10:
                wormhole[arr[x][y]].append((x,y))

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                for dir in range(4):
                    result = max(result, pinbole(x,y,dir))
    print('#{} {}'.format(tc+1,result))