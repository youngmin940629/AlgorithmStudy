def comb(n, m, s=''):
    if m == 0: print(s)
    else:
        for i in range(n, N+1):
            if V[i] == 0:
                comb(i, m-1, s + str(i) + ' ')


N, M = map(int, input().split())
V = [0] * (N+1)
comb(1, M)