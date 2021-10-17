from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def solve():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited = [[[0, 0] for j in range(M)] for i in range(N)]
    dq = deque()
    dq.append([0, 0, 1])
    visited[0][0][0] = 1

    while dq:
        loc = dq.popleft()
        i, j, b = loc[0], loc[1], loc[2]
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '1' and b and not visited[ni][nj][1]:
                visited[ni][nj][1] = visited[i][j][0] + 1
                dq.append([ni, nj, b-1])
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '0' and not b and not visited[ni][nj][1]:
                visited[ni][nj][1] = visited[i][j][1] + 1
                dq.append([ni, nj, b])
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '0' and b and not visited[ni][nj][0]:
                visited[ni][nj][0] = visited[i][j][0] + 1
                dq.append([ni, nj, b])

    if visited[N-1][M-1][0] and visited[N-1][M-1][1]:
        if visited[N-1][M-1][0] > visited[N-1][M-1][1]:
            print(visited[N-1][M-1][1])
        else:
            print(visited[N-1][M-1][0])
    else:
        if visited[N-1][M-1][0]:
            print(visited[N-1][M-1][0])
        elif visited[N-1][M-1][1]:
            print(visited[N-1][M-1][1])
        else:
            print(-1)

solve()