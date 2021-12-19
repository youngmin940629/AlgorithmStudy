import sys;sys.stdin = open('17070.txt')

def solve():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[[0]*3 for _ in range(N)] for __ in range(N)]
    visited[0][1][0] = 1

    for i in range(N):
        for j in range(N):
            if (i == 0 and j == 0) or (i == 0 and j == 1): continue
            if arr[i][j]: continue
            if 0 <= j - 1:
                visited[i][j][0] = visited[i][j-1][0] + visited[i][j-1][2]
            if 0 <= i - 1:
                visited[i][j][1] = visited[i-1][j][1] + visited[i-1][j][2]
            if 0 <= j - 1 and 0 <= i - 1 and not arr[i-1][j] and not arr[i][j-1]:
                visited[i][j][2] = visited[i-1][j-1][0] + visited[i-1][j-1][1] + visited[i-1][j-1][2]

    print(sum(visited[N-1][N-1]))

solve()