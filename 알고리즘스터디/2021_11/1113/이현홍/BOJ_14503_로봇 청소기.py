# 0: 북쪽, 1: 동쪽, 2, 남쪽, 3, 서쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def CLN(r, c, d):
    global cnt
    # 1번 조건은 무조건 실행
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    
    # 왼쪽으로 돌리기
    for x in range(1,5):
        k = (d+4-x)%4
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            # 진행하면 리턴으로 재귀
            return CLN(nr, nc, k)
    
    # 리턴문 안 만난다 = 4방향 모두 청소 불가
    nr = r - dr[d]
    nc = c - dc[d]
    # 뒷 방향이 벽이 아니면 돌아가기
    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 2:
        CLN(nr, nc, d)

# 가로 세로 주의..
M, N = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
CLN(R, C, D)
print(cnt)