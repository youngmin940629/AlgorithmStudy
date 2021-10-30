import sys;sys.stdin = open('2806.txt')

def DFS(k):
    if k >= N:
        global cnt
        cnt += 1
        return
    for i in range(N):
        if col[i]: continue
        flag = False
        for j in range(k):
            x, y = i + (k - j), i - (k - j)
            if 0 <= x < N and rcol[j][x]:
                flag = True
                break
            if 0 <= y < N and rcol[j][y]:
                flag = True
                break
        if flag: continue
        col[i] = 1
        rcol[k][i] = 1
        DFS(k + 1)
        col[i] = 0
        rcol[k][i] = 0

for tc in range(int(input())):
    N = int(input())

    col = [0] * N
    rcol = [[0]*N for _ in range(N)]
    cnt = 0

    DFS(0)
    print(f'#{tc+1} {cnt}')