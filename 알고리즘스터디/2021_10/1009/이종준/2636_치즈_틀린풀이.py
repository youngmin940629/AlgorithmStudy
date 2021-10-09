# 이렇게 하면 치즈안의 구멍까지도 영향을 미치게 되어 실패!

import sys; sys.stdin = open('2636.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

hour = 0
cnt_list = []
while True:
    tmp = 0    
    breaker = False
    # 녹을 부분을 숫자 2로 바꾸기
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if board[nr][nc] == 0:
                        board[r][c] = 2
                        break
    # 안 녹은 부분은 카운팅 하고 2를 0으로 바꾸기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                breaker = True
                board[i][j] = 0
            elif board[i][j] == 1:
                tmp += 1
    
    if breaker == False:
        break
    # 시간 증가
    hour += 1
    cnt_list.append(tmp)

print(hour)
print(cnt_list)