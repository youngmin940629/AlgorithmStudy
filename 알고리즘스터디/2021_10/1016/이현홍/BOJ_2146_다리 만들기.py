import sys
sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# Q 쓰면 깊이 초과 X
def island(r, c):
    global rear
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c]
                island(nr, nc)
            elif arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c]
                rear += 1
                Q[rear] = (nr, nc, 1)
                V[nr][nc] = 1
            elif arr[nr][nc] < 0 and arr[nr][nc] != arr[r][c]:
                global answer 
                answer= 1
                

def BFS(r, c, n):
    global rear, answer
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c]
                V[nr][nc] = n+1
                rear += 1
                Q[rear] = (nr, nc, n+1)
            elif arr[nr][nc] != arr[r][c]:
                answer = V[nr][nc] + V[r][c]

                


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

Q = [0] * N * N
front = -1
rear = -1
V = [[0]*N for _ in range(N)]
answer = 0


cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            cnt -= 1
            arr[r][c] = cnt
            island(r, c)


while answer == 0:
    front +=1
    if BFS(Q[front][0], Q[front][1], Q[front][2]): break

print(answer)