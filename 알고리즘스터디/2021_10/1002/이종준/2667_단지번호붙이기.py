import sys; sys.stdin = open('2667.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def house_cnt():
    global cnt_list    
    count = 0
    while q:
        count += 1
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and houses[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))                
                visited[nr][nc] = 1
    cnt_list.append(count)
    return 1


N = int(input())

houses = [list(map(int, input())) for _ in range(N)]

num_of_block = 0
cnt_list = []
visited = [[0] * N for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(N):
        if houses[i][j] and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
            num_of_block += house_cnt()
cnt_list.sort()
print(num_of_block)
for i in cnt_list:
    print(i)