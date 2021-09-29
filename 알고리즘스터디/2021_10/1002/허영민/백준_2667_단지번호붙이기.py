N = int(input())
data = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
S = []
cnt1 = 0
result = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def isSafe(a,b):
    return 0 <= a < N and 0 <= b < N
def dfs(a,b):
    global cnt_home
    visited[b][a] = 1
    S.append([a, b])
    for dir in range(4):
        next_x, next_y = a + dx[dir], b + dy[dir]
        if isSafe(next_x, next_y) and not visited[next_y][next_x] and data[next_y][next_x] == '1':
            cnt_home += 1
            dfs(next_x, next_y)
    else:
        S.pop()

for y in range(N):
    for x in range(N):
        if data[y][x] == '1' and not visited[y][x]:
            cnt_home = 1
            dfs(x, y)
            result.append(cnt_home)
            cnt1 += 1
print(cnt1)
for i in range(len(result)-1, 0, -1):
    for j in range(i):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
for _ in range(len(result)):
    print(result[_])