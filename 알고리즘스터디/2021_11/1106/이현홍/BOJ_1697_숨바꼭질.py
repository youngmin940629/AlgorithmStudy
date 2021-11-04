N, K = map(int, input().split())

V = [0] * 1000000
Q = [0] * 1000000
f = -1
r = -1

r += 1
Q[r] = N
V[N] = 1

ans = 0
while f != r:
    f += 1
    p = Q[f]
    n = V[p] + 1
    if p < K and V[p+1] == 0:
        V[p+1] = n
        r += 1
        Q[r] = p + 1
    if p * 2 < K * 2 and V[p*2] == 0 :
        V[p*2] = n
        r += 1
        Q[r] = p * 2
    if 0 < p and V[p-1] == 0:
        V[p-1] = n
        r += 1
        Q[r] = p - 1
    
    if V[K]: break

print(V[K]-1)