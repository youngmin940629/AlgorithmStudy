def comb(n, m, s=''):
    if m == 0: print(s)
    else:
        for i in range(n, N+1):
            if V[i] == 0:
                V[i] = 1
                comb(i+1, m-1, s + str(i) + ' ')
                V[i] = 0

N, M = map(int, input().split())

V = [0] * (N+1)
comb(1, M)