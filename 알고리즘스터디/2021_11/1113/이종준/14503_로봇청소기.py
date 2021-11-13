from collections import deque

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    global ans
    while q:
        # 큐에서 빼냄
        r, c, dir = q.popleft()

        # 네 방향 탐색: 첫 왼쪽
        nr = r + dr[(dir - 1 + 4) % 4]
        nc = c + dc[(dir - 1 + 4) % 4]
        if arr[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = 1
            ans += 1
            q.append((nr, nc, (dir - 1 + 4) % 4))
        else:
            # 두번째 왼쪽
            nr = r + dr[(dir - 2 + 4) % 4]
            nc = c + dc[(dir - 2 + 4) % 4]
            if arr[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                ans += 1
                q.append((nr, nc, (dir - 2 + 4) % 4))
            else:
                # 세번째 왼쪽
                nr = r + dr[(dir - 3 + 4) % 4]
                nc = c + dc[(dir - 3 + 4) % 4]
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    ans += 1
                    q.append((nr, nc, (dir - 3 + 4) % 4))
                else:
                    # 마지막 왼쪽 = 원래 방향
                    nr = r + dr[(dir - 4 + 4) % 4]
                    nc = c + dc[(dir - 4 + 4) % 4]
                    if arr[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        ans += 1
                        q.append((nr, nc, dir))
                    # 후진할 수 있으면 후진
                    else:
                        nr = r + dr[(dir - 2 + 4) % 4]
                        nc = c + dc[(dir - 2 + 4) % 4]
                        if arr[nr][nc] == 0:
                            q.append((nr, nc, dir))
                        elif arr[nr][nc] == 1:
                            break


N, M = map(int, input().split())
r, c, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 청소한 구역 수를 저장할 변수 ans
ans = 1

# 방문체크용 배열 초기화
visited = [[0] * M for _ in range(N)]

q = deque()
visited[r][c] = 1
q.append((r, c, dir))
bfs()

print(ans)