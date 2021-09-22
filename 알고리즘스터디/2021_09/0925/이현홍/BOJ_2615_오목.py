o_arr = [[0] * 21 for _ in range(21)]

for i in range(19):
    o_arr[i + 1] = [0] + list(map(int, input().split())) + [0]

def Omok(arr):
    #가로 직선
    for y in range(1, 20):
        for x in range(1, 16):
            if arr[y][x] != 0:
                if arr[y][x-1] != arr[y][x] and arr[y][x+5] != arr[y][x] and arr[y][x] == arr[y][x+1] == arr[y][x+2] == arr[y][x+3] == arr[y][x+4]:
                    return arr[y][x], y, x
    #세로 직선
    for y in range(1, 16):
        for x in range(1, 20):
            if arr[y][x] != 0:
                if arr[y-1][x] != arr[y][x] and arr[y+5][x] != arr[y][x] and arr[y][x] == arr[y+1][x] == arr[y+2][x] == arr[y+3][x] == arr[y+4][x]:
                    return arr[y][x], y, x
    #아래 대각
    for y in range(1, 16):
        for x in range(1, 16):
            if arr[y][x] != 0:
                if arr[y-1][x-1] != arr[y][x] and arr[y+5][x+5] != arr[y][x] and arr[y][x] == arr[y+1][x+1] == arr[y+2][x+2] == arr[y+3][x+3] == arr[y+4][x+4]:
                    return arr[y][x], y, x
    #위 대각
    for y in range(4, 20):
        for x in range(1, 16):
            if arr[y][x] != 0:
                if arr[y+1][x-1] != arr[y][x] and arr[y-5][x+5] != arr[y][x] and arr[y][x] == arr[y-1][x+1] == arr[y-2][x+2] == arr[y-3][x+3] == arr[y-4][x+4]:
                    return arr[y][x], y, x

    return 0

if Omok(o_arr) == 0:
    print(0)

else:
    print(Omok(o_arr)[0])
    print(Omok(o_arr)[1], Omok(o_arr)[2])
