nums = tuple(tuple(input().split()) for _ in range(5))
ans = []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# Visit 없는 DFS
def DFS(r, c, s='', n=0):
    if n == 6:
        ans.append(s)
    else:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5:
                DFS(nr, nc, s+nums[nr][nc], n+1)

# 다 집어넣고
for r in range(5):
    for c in range(5):
        DFS(r, c)

# set처리해서 len 출력
ans = set(ans)
print(len(ans))