from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
population = [0] * (N**2 + 1)
area = [[] for _ in range(N**2 + 1)]

def BFS(i, j):
    global cnt
    di = (1, -1, 0, 0)
    dj = (0, 0, 1, -1)
    dq = deque()
    dq.append((i, j))
    visited[i][j] = cnt
    population[cnt] += arr[i][j]
    area[cnt].append((i, j))
    cnt += 1
    while dq:
        i, j = dq.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if abs(arr[i][j]-arr[ni][nj]) > R or abs(arr[i][j]-arr[ni][nj]) < L: continue
            union = visited[i][j]
            visited[ni][nj] = union
            population[union] += arr[ni][nj]
            area[union].append((ni, nj))
            dq.append((ni, nj))

res = 0
while True:
    cnt = 1
    flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)

    for i in range(1, len(population)):
        if len(area[i]) > 1:
            flag = True
            for j in range(len(area[i])):
                y, x = area[i][j][0], area[i][j][1]
                arr[y][x] = population[i]//len(area[i])

    if not flag: break
    res += 1
    visited = [[0] * N for _ in range(N)]
    population = [0] * (N ** 2 + 1)
    area = [[] for _ in range(N ** 2 + 1)]

print(res)