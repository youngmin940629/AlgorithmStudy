from collections import deque

def bfs():
    while q:
        x,y,check = q.popleft()
        if check == 0 and (x == 0 or x == w -1 or y == 0 or y == h - 1):
            return visited[y][x]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if check == 1 and data[ny][nx] == '.':
                    visited[ny][nx] = -1
                    q.append((nx,ny,check))
                elif check == 0 and data[ny][nx] == '.':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx,ny,check))
    return 'IMPOSSIBLE'

for tc in range(int(input())):
    w, h = map(int, input().split())
    data = [list(input()) for _ in range(h)]
    q = deque()
    fire = []
    person = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            if data[y][x] == '*':
                fire.append((x,y,1))
                visited[y][x] = -1
            elif data[y][x] == '@':
                person.append((x,y,0))
                visited[y][x] = 1
    q.extend(fire)
    q.extend(person)
    print(bfs())