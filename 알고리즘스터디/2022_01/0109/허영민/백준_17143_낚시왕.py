def fishing():
    global st, arr
    st += 1
    hunting(st)
    shark = []
    tmp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if arr[x][y] != 0:
                shark.append([x,y,arr[x][y]])
    move(shark, tmp)
    arr = [tmp[i][:] for i in range(R)]

def move(sharks, sea_arr):
    for srk in sharks:
        shark_x, shark_y = srk[0], srk[1]
        for _ in range(srk[2][0]):
            shark_x += dx[srk[2][1]]
            shark_y += dy[srk[2][1]]
            if 0 > shark_x or shark_x >= R or 0 > shark_y or shark_y >= C:
                if srk[2][1] == 1:
                    srk[2][1] = 2
                elif srk[2][1] == 2:
                    srk[2][1] = 1
                elif srk[2][1] == 3:
                    srk[2][1] = 4
                elif srk[2][1] == 4:
                    srk[2][1] = 3
                shark_x, shark_y = shark_x + (2 * dx[srk[2][1]]), shark_y + (2 * dy[srk[2][1]])
        if sea_arr[shark_x][shark_y] != 0 and sea_arr[shark_x][shark_y][2] > srk[2][2]:
            continue
        else:
            sea_arr[shark_x][shark_y] = [srk[2][0],srk[2][1],srk[2][2]]



def hunting(n):
    global result
    for i in range(R):
        if arr[i][n] != 0:
            result += arr[i][n][2]
            arr[i][n] = 0
            return
    return


R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    arr[r-1][c-1] = [s,d,z]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
st = -1
result = 0
for _ in range(C):
    fishing()

print(result)
