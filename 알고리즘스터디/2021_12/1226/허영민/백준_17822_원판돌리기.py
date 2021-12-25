from collections import deque

def circle_rotation(rotation_arr):
    st_x, d, k = rotation_arr[0], rotation_arr[1], rotation_arr[2]
    x = st_x
    while x <= N:
        if d == 0:
            tmp = [0] * M
            for idx in range(M):
                tmp[idx] = circle[x-1][(idx-k)%M]
            circle[x-1] = tmp
        elif d == 1:
            tmp = [0] * M
            for idx in range(M):
                tmp[idx] = circle[x - 1][(idx + k) % M]
            circle[x - 1] = tmp
        x += st_x

def erase():
    flag = 0
    visited = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if circle[x][y] != 'X':
                visited[x][y] = 1
                q.append((x,y,circle[x][y]))
                while q:
                    r,c,num = q.popleft()
                    for dir in range(4):
                        nr, nc = r + dx[dir], c + dy[dir]
                        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                            if circle[nr][nc] == num:
                                q.append((nr,nc,num))
                                circle[r][c] = 'X'
                                circle[nr][nc] = 'X'
                                visited[nr][nc] = 1
                                flag = 1
                        if nc == M and not visited[nr][0]:
                            if circle[nr][0] == num:
                                q.append((nr, 0, num))
                                circle[r][c] = 'X'
                                circle[nr][0] = 'X'
                                visited[nr][0] = 1
                                flag = 1
                        if nc < 0 and not visited[nr][M-1]:
                            if circle[nr][M-1] == num:
                                q.append((nr, M-1, num))
                                circle[r][c] = 'X'
                                circle[nr][M-1] = 'X'
                                visited[nr][M-1] = 1
                                flag = 1
    return flag

N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
rotation = [list(map(int, input().split())) for _ in range(T)]
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
for rotation_arr in rotation:
    circle_rotation(rotation_arr)
    check = erase()
    if check == 0:
        tmp_sum = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if type(circle[i][j]) == int:
                    tmp_sum += circle[i][j]
                    cnt += 1
        if cnt == 0:
            break
        else:
            tmp_average = tmp_sum / cnt
            for i in range(N):
                for j in range(M):
                    if type(circle[i][j]) == int:
                        if tmp_average < circle[i][j]:
                            circle[i][j] -= 1
                        elif tmp_average > circle[i][j]:
                            circle[i][j] += 1
for x in range(N):
    for y in range(M):
        if type(circle[x][y]) == int:
            result += circle[x][y]

print(result)