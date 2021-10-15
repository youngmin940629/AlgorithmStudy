import sys
sys.stdin = open('sample2.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c, code = 0):
    global r1, r2
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 사람 BFS
        if code:
            arr[r][c] = Q2[f2][2]
            # 좌표 밖으로 탈출할 수 있으면 answer = arr[r][c] ----- (1부터 시작해서 +1 안 함)
            if not (0 <= nr < h and 0 <= nc < w):
                global answer
                answer = -Q2[f2][2]
                # 반복문 끝내기
                return 1
            else:
                # 배열 내에서 움직이면, 새 좌표값이 0이거나 불보다 빨리 도착해야 진행
                if arr[nr][nc] == 0 or arr[nr][nc] < arr[r][c] - 1 < 0:
                    arr[nr][nc] = arr[r][c] - 1
                    r2 += 1
                    Q2[r2] = (nr, nc, Q2[f2][2] -1)
        # 불 BFS
        else:
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] - 1
                r1 += 1
                Q1[r1] = (nr, nc)

for tc in range(1, int(input())+1):
    w, h = map(int, input().split())
    arr = [[0] * w for _ in range(h)]

    # 큐는 크기와 진행순서를 고려해 따로 만듦
    Q1 = [0] * w * h
    f1 = -1
    r1 = -1
    Q2 = [0] * w * h
    f2 = -1
    r2 = -1

    # 출구를 못 찾을 경우 기본 정답
    answer = 'IMPOSSIBLE'

    # 벽은 1, 불은 -1, 공간은 0으로 받았고 사람은 시작점을 별도로 큐에 -1로 저장하고 0으로 함(불 BFS에 방해됨)
    for r in range(h):
        s = input()
        for c in range(w):
            k = s[c]
            if k == '#': k = 1
            elif k == '.': k = 0
            elif k == '@':
                k = 0
                r2 += 1
                Q2[r2] = (r, c, -1)
            elif k == '*':
                k = -1
                r1 += 1
                Q1[r1]=(r, c, 0)
            arr[r][c] = k
    
    # 불 BFS
    while f1 != r1:
        f1 += 1
        BFS(Q1[f1][0], Q1[f1][1])
    
    # 사람 BFS
    while f2 != r2:
        f2 += 1
        if BFS(Q2[f2][0], Q2[f2][1], 1): break
    
    print(answer)