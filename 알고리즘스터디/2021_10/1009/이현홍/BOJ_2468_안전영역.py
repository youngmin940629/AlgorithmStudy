import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c, k):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] > k and visited[nr][nc] == 0:
            BFS(nr, nc, k)  

answer = 1
k = 0
# 물에 전부 잠길 때까지 실행
flag = 1
while flag:
    k += 1
    visited = [[0] * n for _ in range(n)]
    # 영역 크기 + 실행 확인
    tmp = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] - k > 0 and visited[r][c] == 0:
                tmp += 1
                BFS(r, c, k)
    if tmp > answer: answer = tmp
    if tmp == 0: flag = 0
print(answer)

