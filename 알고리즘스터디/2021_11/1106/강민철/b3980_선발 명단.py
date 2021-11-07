import sys;sys.stdin = open('3980.txt')

def DFS(k, acc):
    if k >= N:
        global maxi
        if acc > maxi:
            maxi = acc
        return
    for i in range(N):
        if not arr[k][i]: continue
        if used[i]: continue
        used[i] = 1
        DFS(k+1, acc+arr[k][i])
        used[i] = 0


for tc in range(int(input())):
    N = 11
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0
    used = [0] * N

    DFS(0, 0)
    print(maxi)