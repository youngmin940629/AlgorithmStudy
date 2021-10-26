def comb(n, m, s=''):
    if m == 0: print(s)
    else:
        for i in range(n, N+1):
            comb(i+1, m-1, s + str(i) + ' ')

N, M = map(int, input().split())
comb(1, M)