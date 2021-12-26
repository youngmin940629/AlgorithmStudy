from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):              # bfs 하고 
    q = deque()
    q.append([i, j])
    lst = []
    lst.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L <= abs(s[nx][ny] - s[x][y]) <= R:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    lst.append([nx, ny])
    return lst
dx = [-1, 1, 0, 0]      # 상하좌우순 bfs
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
s = [list(map(int,input().split())) for _ in range(N)]      
cnt = 0
while True:
    visit = [[0] * N for i in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                lst = bfs(i, j)
                if len(lst) > 1:
                    flag = True
                    num = sum([s[x][y] for x, y in lst]) // len(lst)
                    for x, y in lst:
                        s[x][y] = num
    if not flag:
        break
    cnt += 1
print(cnt)