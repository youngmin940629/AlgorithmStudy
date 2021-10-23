import sys; sys.stdin=open('BOJ_15649_N,M.txt','r')

n, m = map(int,input().split())
visited = [0] * n
lst = []
def dfs(d):
    if d == m:
        print(' '.join(map(str,lst)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            lst.append(i+1)
            dfs(d+1)
            visited[i] = 0
            lst.pop()
dfs(0)