import sys
sys.setrecursionlimit(10**5)

# L <= 인구차 <= R: 국경 개방
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c):
    global num, cnt, mark
    V[r][c] = mark
    num += arr[r][c]
    cnt += 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and V[nr][nc] == 0:
            if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                BFS(nr, nc)

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
flag = 1
day = 0
while flag:
    flag = 0
    V = [[0]* N for _ in range(N)]
    mark = 0
    union = {}
    for r in range(N):
        for c in range(N):
            if V[r][c] == 0:
                mark += 1
                num = 0
                cnt = 0
                BFS(r, c)
                union[mark] = num // cnt
    for r in range(N):
        for c in range(N):
            if arr[r][c] != union[V[r][c]]:
                flag = 1
                arr[r][c] = union[V[r][c]]
    if flag: day += 1


print(day)

