dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cctv = {
    1: [0],
    2: [0, 2],
    3: [0, 3], 
    4: [0, 2, 3],
    5: [0, 1, 2, 3],
    6: []
}

# 0이면 CCTV 코드로 변경, CCTV 코드면 0으로 변경
def see(r, c, d):
    change = 0
    n = 0
    while True:
        n += 1
        nr = r + dr[d] * n
        nc = c + dc[d] * n
        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] == 6: break
            if arr[nr][nc] == 0:
                arr[nr][nc] = 10*(r+1) + (c+1)
                change += 1
            elif arr[nr][nc] == 10*(r+1) + (c+1):
                arr[nr][nc] = 0
        else: break
    return change
   

# 재귀
def site(x=0, s=0):
    if x == len(position):
        global marked
        if marked < s:
            marked =s
    else:
        r = position[x][0]
        c = position[x][1]
        lst = cctv[position[x][2]]
        for  i in range(4):
            a = 0
            # CCTV에서 감시 방향에 따라 변경
            for l in lst:
                d = (l+i) % 4
                a += see(r, c, d)
            # 다음 CCTV 진행
            site(x+1, s+a)
            # 감시 방향 초기화
            for l in lst:
                d = (l+i) % 4
                see(r, c, d)
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

space = 0
position = []
marked = 0
for r in range(R):
    for c in range(C):
        if arr[r][c]:
            if arr[r][c] != 6:
                position.append((r, c, arr[r][c]))
        elif arr[r][c] == 0:
            space += 1

site()
print(space - marked)