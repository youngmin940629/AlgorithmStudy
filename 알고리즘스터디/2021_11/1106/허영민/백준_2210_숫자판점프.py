from collections import deque

def bfs():
    while q:
        x,y,num = q.popleft()
        if len(num) == 6:
            if num not in result:
                result.add(num)
        elif len(num) < 6:
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    q.append((nx,ny,num + data[nx][ny]))

data = [list(map(str, input().split())) for _ in range(5)]
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = set()
for x in range(5):
    for y in range(5):
        q.append((x,y,''))
bfs()
print(len(result))