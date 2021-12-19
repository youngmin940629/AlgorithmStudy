import sys
input=sys.stdin.readline

def dfs(r,c,d):
    global ans
    if r == n-1 and c == n-1:
        ans += 1
        return
    
    if d == 0 or d == 2:
        if c + 1 < n:
            if a[r][c+1] == 0:
                dfs(r, c+1, 0)
    if d == 1 or d == 2:
        if r + 1 < n:
            if a[r+1][c] == 0:
                dfs(r+1, c, 1)
    if d == 0 or d == 1 or d == 2:
        if r+1 < n and c+1 < n:
            if a[r+1][c] == 0 and a[r][c+1] == 0 and a[r+1][c+1] == 0:
                dfs(r+1, c+1, 2)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs = (0, 1, 0)
print(ans)
