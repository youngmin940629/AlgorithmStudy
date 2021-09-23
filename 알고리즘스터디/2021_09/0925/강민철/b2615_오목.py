import sys;sys.stdin = open('2615.txt')

arr = [list(map(int, input().split())) for i in range(19)]

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

res = resi = resj = 0

def search(i, j, n, k, d):
    if n > 5:
        return 0
    if n == 1:
        ni = i-di[d]
        nj = j-dj[d]
        if 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == k:
            return 0
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == k:
        if search(ni, nj, n + 1, k, d):
            return k
    else:
        if n == 5:
            return k
    return 0

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            for d in range(4):
                res = search(i, j, 1, arr[i][j], d)
                if res:
                    resi = i+1
                    resj = j+1
                    break
        if res:
            break
    if res:
        break

if res:
    print(res)
    print(resi, resj)
else:
    print(0)