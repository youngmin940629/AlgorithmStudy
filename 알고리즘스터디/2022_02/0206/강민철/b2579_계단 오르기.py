def solve():
    N = int(input())
    S = [0] * (N+1)

    for i in range(1, N+1):
        S[i] = int(input())

    D = [[0]*3 for _ in range(N+1)]

    if N == 1:
        return S[N]

    D[1][1], D[2][1], D[2][2] = S[1], S[2], S[1]+S[2]

    for i in range(3, N+1):
        D[i][1] = max(D[i-2][1], D[i-2][2]) + S[i]
        D[i][2] = D[i-1][1] + S[i]

    return max(D[N][1], D[N][2])

print(solve())