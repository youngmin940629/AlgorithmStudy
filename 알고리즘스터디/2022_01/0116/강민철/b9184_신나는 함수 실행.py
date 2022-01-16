cube = [[[0]*21 for _ in range(21)] for __ in range(21)]

for z in range(2):
    for y in range(2):
        for x in range(2):
            if z == 0:
                cube[z][y][x] = 1
                continue
            if y == 0:
                cube[z][y][x] = 1
                continue
            if x == 0:
                cube[z][y][x] = 1
                continue

for z in range(21):
    for y in range(21):
        for x in range(21):
            if cube[z][y][x]: continue
            if z <= 0 or y <= 0 or x <= 0: cube[z][y][x] = 1
            elif x < y < z:
                cube[z][y][x] = cube[z-1][y][x] + cube[z-1][y-1][x] - cube[z][y-1][x]
            else:
                cube[z][y][x] = cube[z][y][x-1] + cube[z][y-1][x-1] + cube[z-1][y][x-1] - cube[z-1][y-1][x-1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
        continue
    if a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {cube[20][20][20]}')
        continue
    print(f'w({a}, {b}, {c}) = {cube[c][b][a]}')