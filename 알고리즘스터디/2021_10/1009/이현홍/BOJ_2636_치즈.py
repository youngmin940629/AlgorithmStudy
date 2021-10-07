# 재귀 깊이 증가 → Q로 구현 또는 재귀x 반복함수로 처리 가능
import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def BFS(r, c, x):
    global flag
    visited[r][c] = 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            # 치즈가 없거나 녹은 공간인 경우 재귀 호출
            if arr[nr][nc] in melted and visited[nr][nc] == 0:
                BFS(nr, nc, x)
            # 치즈가 있는 곳은 표시만 하고 탈출
            elif arr[nr][nc] == 1:
                arr[nr][nc] = x - 1
                cnt[1-x] += 1
                # 녹은 치즈가 있다면 flag 다시 세움
                flag = 1

N, M = map(int, input().split())
arr = [0] * N
for n in range(N):
    arr[n] = list(map(int, input().split()))


flag = 1
melted = [0]
x = 0
# 적당한 배열 생성
cnt = [0] * 100
while flag:
    # 매 수행 전마다 visited 초기화
    visited = [[0] * M for _ in range(N)]
    # 녹은 치즈 없으면 종료
    flag = 0
    # 항상 (0, 0)에서 시작 처음 만나는 치즈는 -1, 그 다음은 -2 ...
    BFS(0, 0, x)
    # 녹은 치즈가 있던 장소도 공기가 통하는 공간으로 설정
    x -= 1
    melted.append(x)

# 마지막 빼준 x값은 의미없으므로 다시 +1하고 부호 반전
print(-(x+1))
# 가장 마지막 값 호출
for i in range(99, -1, -1):
    if cnt[i]:
        print(cnt[i])
        break