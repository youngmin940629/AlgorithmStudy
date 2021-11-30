from collections import deque

def diffusion():
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                q.append((i,j,room[i][j]))
    while q:
        x,y,dust = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                room[nx][ny] += dust // 5
                room[x][y] -= dust // 5

def clean():
    for case in range(2):
        if case == 0:
            x = airclean[case]
            for i in range(x-2, -1, -1):
                room[i+1][0] = room[i][0]
            for i in range(1, C):
                room[0][i-1] = room[0][i]
            for i in range(1, x+1):
                room[i-1][C-1] = room[i][C-1]
            for i in range(C-2, 0, -1):
                room[x][i+1] = room[x][i]
            room[x][1] = 0
        elif case == 1:
            x = airclean[case]
            for i in range(x+2 ,R):
                room[i-1][0] = room[i][0]
            for i in range(1, C):
                room[R-1][i-1] = room[R-1][i]
            for i in range(R-2, x-1, -1):
                room[i+1][C-1] = room[i][C-1]
            for i in range(C-2, 0, -1):
                room[x][i+1] = room[x][i]
            room[x][1] = 0


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
airclean = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
for x in range(R):
    if room[x][0] == -1:
        airclean.append(x)
q = deque()
for _ in range(T):
    diffusion()
    clean()

for x in range(R):
    for y in range(C):
        if room[x][y] > 0:
            result += room[x][y]
print(result)