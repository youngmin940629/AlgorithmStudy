import sys; sys.stdin = open('2667.txt', 'r')
from collections import deque

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 한 개의 단지 구성 및 단지 내 집 수 카운팅
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

# N*N 입력
N = int(input())

# 지도 입력
houses = [list(map(int, input())) for _ in range(N)]

# 단지 수
num_of_block = 0

# 단지 내 집의 수들을 추가할 리스트 생성
cnt_list = []

# 방문처리할 리스트
visited = [[0] * N for _ in range(N)]

# 큐 생성
q = deque()

# 지도 돌면서 집이 있는 위치(1)가 방문 안 됐으면 함수 실행
for i in range(N):
    for j in range(N):
        if houses[i][j] and not visited[i][j]:
            visited[i][j] = 1
            q.append((i, j))
            num_of_block += house_cnt()

# 집의 수 오름차순 정렬
cnt_list.sort()

# 출력 부분
print(num_of_block)
for i in cnt_list:
    print(i)