def shoot(height, width, arr):
    for x in range(1, D+1):
        for l in range(x, -1,- 1):
            h = x - l
            if h > 0 and 0 <= height - h < N and 0 <= width - l < M and arr[height-h][width-l] == 1:
                return (height- h, width - l)
        for r in range(1, x+1, 1):
            h = x - r
            if h > 0 and 0 <= height - h < N and 0 <= width + r < M and arr[height-h][width+r] == 1:
                return (height- h, width + r)
    return None


def defence(achors_arr):
    global tmp_cnt
    for x in range(N,0,-1):
        villain = set()
        for achor_position in achors_arr:
            killed = shoot(x,achor_position,tmp_castle)
            if killed != None:
                villain.add(killed)
        for killed_villain in villain:
            if tmp_castle[killed_villain[0]][killed_villain[1]] == 1:
                tmp_castle[killed_villain[0]][killed_villain[1]] = 0
                tmp_cnt += 1

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
result = 0
achor = []
for a in range(M):
    for b in range(a+1,M):
        for c in range(b+1,M):
            achor.append((a,b,c))
for i in range(len(achor)):
    tmp_castle = [castle[row_idx][:] for row_idx in range(N)]
    tmp_cnt = 0
    defence(achor[i])
    result = max(result, tmp_cnt)
print(result)