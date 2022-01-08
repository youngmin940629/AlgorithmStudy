import sys
sys.setrecursionlimit(10**7)

N = int(input())
people = list(map(int, input().split()))
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    node[a].append(b)
    node[b].append(a)
dp = [[0,0] for _ in range(N+1)]
visited = [0] * (N+1)

def DFS(n):
    visited[n] = 1
    dp[n][0] = people[n-1]
    for next in node[n]:
        if not visited[next]:
            DFS(next)
            dp[n][0] += dp[next][1]
            dp[n][1] += max(dp[next][0], dp[next][1])
DFS(1)
print(max(dp[1][0], dp[1][1]))