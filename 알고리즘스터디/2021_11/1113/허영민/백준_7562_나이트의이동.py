from collections import deque

def bfs():
    global result
    while q:
        x, y, cnt = q.popleft()
        if x == end[0] and y == end[1]:
            if result > cnt:
                result = cnt
                return
        else:
            for dir in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny,cnt+1))

for tc in range(int(input())):
    l = int(input())
    st = list(map(int, input().split()))
    end = list(map(int, input().split()))
    result = l * l
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2 ,-1]
    visit = [[0] * l for _ in range(l)]
    q = deque()
    q.append((st[0], st[1], 0))
    bfs()
    print(result)