import sys;sys.stdin = open('2210.txt')

arr = [input().split() for _ in range(5)]

check = set()
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)
def DFS(i, j, k, acc:str):
    if k >= 6:
        if acc not in check:
            check.add(acc)
        return
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if ni < 0 or ni >= 5 or nj < 0 or nj >= 5: continue
        DFS(ni, nj, k+1, acc+arr[ni][nj])

for i in range(5):
    for j in range(5):
        DFS(i, j, 1, arr[i][j])

print(len(check))