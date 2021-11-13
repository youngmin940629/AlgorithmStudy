# 8방향 dir
dr = [2, -1, 2, 1, -2, 1, -1, -2]
ds = [-1, 2, 1, 2, 1, -2, -2, -1]
def knight(r, c, n):
    for k in range(8):
        nr = r + dr[k]
        nc = c + ds[k]
        if 0 <= nr < L and 0 <= nc < L and V[nr][nc] == 0:
            inid = abs(er-sr) +abs(ec-sc)
            nd = abs(er-nr) + abs(ec-nc)
            # 어느 정도 가까워 질때 까지는 거리가 멀어지는 경우 제외
            if nd < inid or nd < 5:
                V[nr][nc] = n+1
                Q.append((nr, nc, n+1))


for tc in range(1, int(input())+1):
    L = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    if (sr, sc) == (er, ec): print('0')
    else:
        Q = []
        Q.append((sr, sc, 1))
        V = [[0]*L for _ in range(L)]

        idx = -1
        while True:
            idx += 1
            r = Q[idx][0]
            c = Q[idx][1]
            n = Q[idx][2]

            if r == er and c == ec:
                print(n-1)
                break
            knight(r, c, n)