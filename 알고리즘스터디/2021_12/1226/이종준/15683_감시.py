# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def check(r, c, dirs, tmp_data):
    cnt = 0    
    for i in dirs:
        nr = r
        nc = c
        while True:        
            nr += dr[i]
            nc += dc[i]
            if 0 > nr or N <= nr or 0 > nc or M <= nc or tmp_data[nr][nc] == 6: break
            if tmp_data[nr][nc] == 0:
                tmp_data[nr][nc] = '#'
                cnt += 1
    return cnt

def dfs(k, tmp, tmp_map):
    global min_area
    visit = [tmp_map[row][:] for row in range(N)]
    if k == len(cctv):
        if min_area > blank - tmp:
            min_area = blank - tmp
    else:
        r, c, cctv_type = cctv[k]
        for dirs in cctv_dirs[cctv_type]:
            tmp_cnt = check(r, c, dirs, visit)
            dfs(k + 1, tmp + tmp_cnt, visit)
            visit = [tmp_map[row][:] for row in range(N)]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

cctv_dirs = [
    [], 
    [[0], [1], [2], [3]], 
    [[0, 2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [3, 0]], 
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 
    [[0, 1, 2, 3]]
]

min_area = 987654321
blank = 0

cctv = []
for i in range(N):
    for j in range(M):
        if data[i][j] in range(1, 6):
            c_type = data[i][j]
            cctv.append((i, j, c_type))
        elif data[i][j] == 0:
            blank += 1

dfs(0, 0, data)

print(min_area)