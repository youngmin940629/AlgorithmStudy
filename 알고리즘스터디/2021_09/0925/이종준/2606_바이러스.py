'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
# 정점 수
V = int(input())

# 간선 수
E = int(input())

#인접 행렬
G = [[0] * (V+1) for _ in range(V+1)]

# 방문처리 초기화
visited = [0] * (V + 1)

# 간선들 인접행렬에 입력
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

cnt = 0

def dfs(n):
    global cnt
    visited[n] = 1
    for w in range(1, V + 1):
        if G[n][w] == 1 and not visited[w]:
            cnt += 1
            dfs(w)

dfs(1)
print(cnt)