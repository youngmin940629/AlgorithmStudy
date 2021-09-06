N = int(input())
arr = [[0] * N for _ in range(N)]
for r in range(N):
    A = input()
    for c in range(N):
        arr[r][c] = A[c]
# 일부러 문자로 받아서 BFS때 숫자 1을 쓸 수 있게 함

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
num = 0
cnt = []

def BFS(r,c):
    arr[r][c] = num
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1':
            arr[nr][nc] = num
            cnt[num - 1] += 1
            BFS(nr, nc)

for r in range(N):
    for c in range(N):
        if arr[r][c] == '1':
            num += 1
            cnt.append(1)
            BFS(r, c)


print(num)
cnt.sort()
for a in cnt:
    print(a)
