import sys
sys.stdin = open('s.txt', 'r')

    # 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def BFS(r, c, d, n, x):
    if r == er and c == ec and d == ed:
        return n
    global rear
    for k in range(4):
        if k == d: continue
        a = 1
        if k+d == 1 or k+d == 5: a = 2
        if V[r][c][k] == 0 or n+a <= V[r][c][k]:
            rear += 1
            Q[rear] = (r, c, k, n+a, 0)
            V[r][c][k] = n + a
        
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
        if x == 0:
            n += 1
            x = 3
        if V[nr][nc][d] == 0 or n <= V[nr][nc][d]:
            rear += 1
            Q[rear] = (nr, nc, d, n, x-1)
            V[nr][nc][d] = n


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sr, sc, sd = map(lambda x: int(x) -1, input().split())
er, ec, ed = map(lambda x: int(x) -1, input().split())

if (sr, sc, sd) == (er, ec, ed):
    print(0)


else:
    V = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    Q = [0] * M * N * 10000
    front = -1
    rear = -1
    rear += 1
    Q[rear] = (sr, sc, sd, 0, 0)
    V[sr][sc][sd] = 1

    while front != rear:
        front += 1
        BFS(Q[front][0], Q[front][1], Q[front][2], Q[front][3], Q[front][4])

    print(V[er][ec][ed])