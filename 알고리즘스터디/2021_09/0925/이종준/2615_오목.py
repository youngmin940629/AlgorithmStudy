### 안풀림 (거친욕) 도와주세요

# 현재 오목판 상태 입력
omok_map = [list(map(int, input().split())) for _ in range(19)]


# 우, 우하, 하, 좌하
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

# 좌, 좌상, 상, 우상
dr_check = [0, -1, -1, -1]
dc_check = [-1, -1, 0, 1]

winner = 0
winner_r = 0
winner_c = 0

def check(r, c, cnt, dir):
    if cnt > 5:
        return 0
    # 시작할 때 좌, 좌상, 상, 우상에 돌 있는지 체크
    if cnt == 1:
        nr = r + dr_check[dir]
        nc = c + dc_check[dir]
        if 0 <= nr < 19 and 0 <= nc < 19 and omok_map[r][c] == omok_map[nr][nc]:
            return 0
    # 오목 달성한 경우 winner 변수에 1 or 2 저장하고 break 걸기

    nr = r + dr[dir]
    nc = c + dc[dir]

    if 0 <= nr < 19 and 0 <= nc < 19 and omok_map[r][c] == omok_map[nr][nc]:
        if check(nr, nc, cnt + 1, dir):
            return omok_map[r][c]
    else:
        if cnt == 5:
            return omok_map[r][c]
    return 0

for i in range(19):
    for j in range(19):
        if omok_map[i][j]:
            # check 함수 안에서 하면 틀릴 수도 있음. 처음부터 한 방향으로만 가기 위해 여기서 방향에 대한 for문 돌림
            for k in range(4):
                winner = check(i, j, 1, k)
                if winner:
                    winner_r = i + 1
                    winner_c = j + 1
                    break
        if winner:
            break
    if winner:
        break

if winner:
    print(winner)
    print(winner_r, winner_c)
else:
    print(0)