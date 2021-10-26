dr=[1, 0, -1, 0, 1, 1, -1, -1]
dc=[0, 1, 0, -1, 1, -1, 1, -1]
def Queen(r, c):                        # 8방향으로 visit 체크하는 함수
    if arr[r][c]: n = -1
    else: n = 1
    arr[r][c] += n
    for i in range(1, N):
        for k in range(8):
            nr = r + dr[k] * i
            nc = c + dc[k] * i
            if 0<= nr < N and 0 <= nc < N: 
                arr[nr][nc] += n


def spot(n=0):
    if n == N:
        global ans
        ans += 1
    else:
        for i in range(N):
            if arr[n][i] == 0:      # 퀸을 놓을 수 있는 자리면 체크 함수 호출
                Queen(n, i)
                spot(n+1)
                Queen(n, i)

for tc in range(1, int(input())+1):
    N = int(input())
    ans = 0
    arr = [[0]*N for _ in range(N)]
    spot()
    print('#{} {}'.format(tc, ans))