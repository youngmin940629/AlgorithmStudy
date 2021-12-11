# 4방향 장애물 검사 함수
def core(r, c):
    v = [1] * 4
    for lx in range(c):
        if arr[r][lx] != 0: v[0] = 0
    for rx in range(c+1, N):
        if arr[r][rx] != 0: v[1] = 0
    for uy in range(r):
        if arr[uy][c] != 0: v[2] = 0
    for dy in range(r+1, N):
        if arr[dy][c] != 0: v[3] = 0
    return v

# 특정 방향 전선 깔기 함수, 리턴값: 전선 칸 수
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def trans(r, c, n, s=0):
    nr = r + dr[n]
    nc = c + dc[n]
    if 0 <= nr < N and 0 <= nc <N:
        if arr[nr][nc] == 0:
            arr[nr][nc] = 3
            return trans(nr, nc, n, s+1)
        elif arr[nr][nc] == 3:
            arr[nr][nc] = 0
            return trans(nr, nc, n)
    return s

# (1, N-1)범위에 있는 프로세서만 돌면서 돌아감
def lining(s=0, n=0, l=0):                  # s 전원 연결, n 인덱스, l 전선
    global powered, line
    if len(arm) - n + s < powered: return   # 백트래킹
    if n == len(arm):
        if (powered == s and l < line) or powered < s:  
            powered = s
            line = l
    else:
        r, c = arm[n]
        v = core(r, c)
        for i in range(4):              # 완전탐색
            if v[i]:
                k = trans(r, c, i)      # 전선 깔고
                lining(s+1, n+1, l+k)   # 다음
                trans(r, c, i)          # 전선 지우고
        lining(s, n+1, l)               # 넘어가기

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    side = []
    arm = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                if 0 < r < N and 0 < c < N: arm.append((r, c))
                else: side.append((r, c))
    powered = 0
    line = 0
    lining(len(side))                   # 사이드쪽 프로세서 수 포함
    print('#{} {}'.format(tc, line))