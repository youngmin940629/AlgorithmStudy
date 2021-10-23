import sys
sys.stdin = open('s.txt', 'r')

    # 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# 좌표, 방향, 동작횟수, 에너지
def BFS(r, c, d, n, x):
    if r == er and c == ec and d == ed:
        return n
    global rear
    
    # 방향 돌리기
    for k in range(4):
        # 들어온 방향과 다를 때,
        if k == d: continue
            
        # 돌리는 방향이 한 칸이면 1, 두 칸이면 2를 동작횟수에 추가
        a = 1
        if k+d == 1 or k+d == 5: a = 2
        
        # Q에 현재 좌표, 돌린 방향, 동작횟수, 에너지 0 추가
        if V[r][c][k] == 0 or n+a <= V[r][c][k]:
            rear += 1
            Q[rear] = (r, c, k, n+a, 0)
            V[r][c][k] = n + a
    
    # 들어온 방향으로 나아갈 때,
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
        # 에너지가 없으면 동작횟수에 +1, 에너지는 3
        if x == 0:
            n += 1
            x = 3
        # 나아간 좌표, 나아간 방향, 동작횟수, 현재 에너지 -1 Q에 추가
        if V[nr][nc][d] == 0 or n <= V[nr][nc][d]:
            rear += 1
            Q[rear] = (nr, nc, d, n, x-1)
            V[nr][nc][d] = n


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1씩 빼서 받기
sr, sc, sd = map(lambda x: int(x) -1, input().split())
er, ec, ed = map(lambda x: int(x) -1, input().split())

# 시작, 출발점 같은 경우 동작 0
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
