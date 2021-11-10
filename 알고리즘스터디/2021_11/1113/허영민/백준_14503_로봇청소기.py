import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def robot(x,y,dir,cnt,case,check):
    if case == 1:
        arr[x][y] = 2
        cnt += 1
        case = 2
    if case == 2:
        if check == 4:
            next_dir = (dir - 2) % 4
            nx, ny = x + dx[next_dir], y + dy[next_dir]
            if arr[nx][ny] == 2:
                return robot(nx,ny,dir,cnt,2,0)
            else:
                return cnt
        else:
            next_dir = (dir - 1) % 4
            nx, ny = x + dx[next_dir], y + dy[next_dir]
            if arr[nx][ny] == 0:
                return robot(nx,ny,next_dir,cnt,1,0)
            else:
                return robot(x,y,next_dir,cnt,2,check+1)

print(robot(r,c,d,0,1,0))