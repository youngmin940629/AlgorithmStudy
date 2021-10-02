import sys; sys.stdin = open('1012.txt', 'r')

T = int(input())

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def worm(r, c):
    global visited
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] and not visited[nr][nc]:
            worm(nr, nc)
    return 1


for _ in range(T):
    M, N, E = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    for _ in range(E):
        s, e = map(int, input().split())
        field[e][s] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                result += worm(i, j)

    print(result)

    # recursionError 뜸 => 재귀가 너무 깊어진다는 뜻
    # 만약 전체 필드가 1로 덮여있을 경우 재귀가 깊어질 거 같음