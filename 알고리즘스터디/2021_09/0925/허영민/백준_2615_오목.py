data = [list(map(int, input().split())) for _ in range(19)]
rst_x, rst_y = 0, 0
dx=[0, 1, 1, 1]
dy=[1, 1, 0, -1]
check_black = 0
check_white = 0

def is_safe(x,y):
    return 0 <= x < 19 and 0 <= y < 19


def black_omok(x,y,dir,cnt):
    global rst_x, rst_y ,check_black
    if cnt == 5:
        if is_safe(x+dx[dir], y+dy[dir]) and data[y+dy[dir]][x+dx[dir]] == 1:
            return
        elif is_safe(x - 5 * dx[dir], y - 5 * dy[dir]) and data[y-5*dy[dir]][x-5*dx[dir]] == 1:
            return
        else:
            if check_black != 1:
                rst_x, rst_y = x - 4 * dx[dir], y - 4 * dy[dir]
                check_black = 1
                return

    else:
        next_x, next_y = x + dx[dir], y + dy[dir]
        if is_safe(next_x, next_y) and data[next_y][next_x] == 1:
            cnt += 1
            black_omok(next_x, next_y, dir, cnt)


def white_omok(x,y,dir,cnt):
    global rst_x, rst_y, check_white
    if cnt == 5:
        if is_safe(x + dx[dir], y + dy[dir]) and data[y + dy[dir]][x + dx[dir]] == 2:
            return
        elif is_safe(x - 5 * dx[dir], y - 5 * dy[dir]) and data[y - 5 * dy[dir]][x - 5 * dx[dir]] == 2:
            return
        else:
            if check_white != 1:
                rst_x, rst_y = x - 4 * dx[dir], y - 4 * dy[dir]
                check_white = 1
                return
    else:
        next_x, next_y = x + dx[dir], y + dy[dir]
        if is_safe(next_x, next_y) and data[next_y][next_x] == 2:
            cnt += 1
            white_omok(next_x, next_y, dir, cnt)


for y in range(19):
    for x in range(19):
        if data[y][x] == 1:
            for idx in range(4):
                if is_safe(x+dx[idx], y+dy[idx]) and data[y+dy[idx]][x+dx[idx]] == 1:
                    black_omok(x+dx[idx], y+dy[idx], idx, 2)
        elif data[y][x] == 2:
            for idx in range(4):
                if is_safe(x+dx[idx], y+dy[idx]) and data[y+dy[idx]][x+dx[idx]] == 2:
                    white_omok(x+dx[idx], y+dy[idx], idx, 2)


if check_black * check_white == 1:
    print(0)
elif check_black == 1:
    print(1)
    print(rst_y + 1, rst_x + 1)
elif check_white == 1:
    print(2)
    print(rst_y + 1, rst_x + 1)
else:
    print(0)