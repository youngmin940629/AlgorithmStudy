'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
def bingo_check():
    global bingo_cnt
    cnt = 0
    # 오-왼 대각선 빙고 체크
    for i in range(5):
        if data[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        bingo_cnt += 1
        cnt = 0
    else:
        cnt = 0
    # 왼-오 대각선 빙고 체크
    for i in range(5):
        if data[i][i] == 0:
            cnt += 1
    if cnt == 5:
        bingo_cnt += 1
        cnt = 0
    else:
        cnt = 0
    # 가로 방향 빙고 체크
    for i in range(5):
        for j in range(5):
            if data[i][j] == 0:
                cnt += 1
        if cnt == 5:
            bingo_cnt += 1
            cnt = 0
        else:
            cnt = 0
    # 세로 방향 빙고 체크
    for i in range(5):
        for j in range(5):
            if data[j][i] == 0:
                cnt += 1
        if cnt == 5:
            bingo_cnt += 1
            cnt = 0
        else:
            cnt = 0

# 작성한 빙고판
data = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 빙고
mc = [list(map(int, input().split())) for _ in range(5)]
# 최종 출력할 카운트
cnt = 0
# 빙고 개수 셀 변수
bingo_cnt = 0
# for문 최종으로 나오기 위한 변수
bingo_breaker = False

for i in range(5):
    for j in range(5):
        # 사회자가 부르는 숫자를 빙고판에서 찾기
        breaker = False
        for k in range(5):
            for l in range(5):
                # 찾으면 0으로 바꾸고 횟수 세기
                if data[k][l] == mc[i][j]:
                    data[k][l] = 0
                    cnt += 1
                    breaker = True
                    break
            if breaker:
                break
        # 여기서 빙고판 체크
        bingo_check()
        if bingo_cnt >= 3:    # 처음에 ==으로 했다가 틀림... => 2에서 바로 4로 넘어가는 경우 존재
            bingo_breaker = True
            break
        else:
            bingo_cnt = 0
            continue
    if bingo_breaker:
        break
print(cnt)