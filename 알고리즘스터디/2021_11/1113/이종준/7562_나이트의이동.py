from collections import deque

# 나이트가 움직이는 방향
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    global ans
    while q:
        r, c, cnt = q.popleft()
        # 목적지를 만났을 때 카운트를 return함
        if arr[r][c] == 2:
            return cnt

        # 카운트 늘려주면서 이동
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1                
                q.append((nr, nc, cnt + 1))
                

# 최종 출력할 때 이용할 리스트
result = []

# 테스트 케이스 돌면서
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 출발지
    r, c = map(int, input().split())
    arr[r][c] = 1
    # 목적지
    er, ec = map(int, input().split())    
    arr[er][ec] = 2

    # 방문체크할 배열 초기화
    visited = [[0] * N for _ in range(N)]

    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1


    result.append(bfs())

for res in result:
    print(res)