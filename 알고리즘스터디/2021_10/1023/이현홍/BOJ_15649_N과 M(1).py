def comb(m, s=''):
    if m == 0: print(s)
    else:
        for i in range(1, N+1):
            if V[i] == 0:
                V[i] = 1
                comb(m-1, s + str(i) + ' ')
                V[i] = 0

N, M = map(int, input().split())
V = [0] * (N+1)
comb(M)