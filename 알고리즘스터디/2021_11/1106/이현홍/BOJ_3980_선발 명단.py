def ps(n=0, s=0):
    if n == 11:
        global ans
        if ans < s:
            ans = s
    else:
        for i in range(11):
            if P[n][i] != 0 and V[i] == 0:
                V[i] = 1
                ps(n+1, s+P[n][i])
                V[i] = 0

for tc in range(int(input())):
    P = tuple(tuple(map(int, input().split())) for _ in range(11))
    V = [0] * 11
    ans = 0
    ps()
    print(ans)