from collections import deque

def bfs(st):
    q.append([st])
    visited = [0] * (N+1)
    visited[st] = 1
    while q:
        start = q.popleft()[0]
        for nxt in range(N+1):
            if not visited[nxt] and friend[start][nxt] == 1:
                visited[nxt] = visited[start] + 1
                q.append([nxt])
    scores[st] = max(visited)

N = int(input())
friend =[[0] * (N+1) for _ in range(N+1)]
scores = [0] * (N+1)
while True:
    a, b = map(int, input().split())
    if a != -1 and b != -1:
        friend[a][b] = friend[b][a] = 1
    else:
        break
q = deque()
for i in range(1, N+1):
    bfs(i)
score = min(scores[1:N+1]) -1
result = []
result_num = 0
for idx in range(1, N+1):
    if score + 1 == scores[idx]:
        result.append(idx)
        result_num += 1
print(score, result_num)
print(' '.join(map(str, result)))