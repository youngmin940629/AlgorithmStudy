import sys; sys.stdin=open('BOJ_10711_모래성.txt','r')
from collections import deque
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
def bfs():
    visited = [[0] * c for _ in range(r)]
    res = 0
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < c and 0 <= ny < r: # and arr[ny][nx] != 0:    # arr[ny][nx] > 0 or arr[ny][nx] != '.'
                if arr[ny][nx] != 0:
                    arr[ny][nx] -= 1
                    if arr[ny][nx] == 0:                                # or arr[ny][nx] == '.'
                        q.append((nx, ny))
                        visited[ny][nx] = visited[y][x] + 1
                        res = max(res, visited[ny][nx])
    return res

r,c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

q = deque()
res = 0
for x in range(c):
    for y in range(r):
        if arr[y][x] == '.':
            q.append((x,y))
            arr[y][x] = 0
        else:
            arr[y][x] = int(arr[y][x])
print(bfs())

# count를 해서 값의 크기를 비교후 값이 적다 하면 . 을 찍고 모두 돌고 나면 cnt += 1 해주기
