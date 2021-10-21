def comb(m, s=''):
    if m == 0: print(s)
    else:
        for i in range(1, N+1):
            if V[i] == 0:
                comb(m-1, s + str(i) + ' ')


N, M = map(int, input().split())
V = [0] * (N+1)
comb(M)