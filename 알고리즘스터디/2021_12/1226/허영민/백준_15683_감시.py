def vision_check(x,y,cctv_direction, tmp_arr):
    cnt = 0
    for direction in cctv_direction:
        nx, ny = x, y
        while True:
            nx += dx[direction]
            ny += dy[direction]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and tmp_arr[nx][ny] != 6:
                if tmp_arr[nx][ny] == 0:
                    tmp_arr[nx][ny] = '#'
                    cnt += 1
            else:
                break
    return cnt

def cctv_check(n, vision_cnt, office_arr):
    global result, nothing
    tmp = [office_arr[i][:] for i in range(N)]
    if n == len(cctv):
        if result > nothing - vision_cnt:
            result = nothing - vision_cnt
    else:
        x, y = cctv[n]
        cctv_number = arr[x][y]
        for cctv_vision in CCTV[cctv_number]:
            tmp_cnt = vision_check(x,y,cctv_vision,tmp)
            cctv_check(n+1, vision_cnt + tmp_cnt, tmp)
            tmp = [office_arr[i][:] for i in range(N)]






N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = N * M
nothing = 0
visited = [[0] * N for _ in range(M)]
CCTV = {
    1 : ([0],[1],[2],[3]),
    2 : ([0,1], [2,3]),
    3 : ([0,2], [1,2], [0,3], [1,3]),
    4 : ([0,1,2], [0,1,3], [0,2,3], [1,2,3]),
    5 : [[0,1,2,3]]
}
cctv = []
for x in range(N):
    for y in range(M):
        if 1 <= arr[x][y] <= 5:
            cctv.append((x,y))
        elif arr[x][y] == 0:
            nothing += 1
cctv_check(0,0, arr)
print(result)