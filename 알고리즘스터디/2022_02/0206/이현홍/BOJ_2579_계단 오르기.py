N = int(input())

# 계단이 3칸 이하일 때
if N < 3:
    a = 0
    for _ in range(N):
        a += int(input())
    print(a)
# 이상일 때
else:
    stairs = [0] * (N)
    for i in range(N):
        stairs[i] = int(input())

    V = [[0, 0] for _ in range(N)]
    V[0] = [stairs[0], stairs[0]]               # V[n][0]는 건너뛰고 시작하는 칸
    V[1] = [stairs[1], stairs[0]+stairs[1]]     # V[n][1]은 두 칸 연속으로 선택한 경우

    for i in range(2, N):
        V[i][0] = max(V[i-2]) + stairs[i]       # 한 칸 건너 뛰므로 둘 중 아무거나 선택
        V[i][1] = V[i-1][0] + stairs[i]         # 연속 선택이므로 한 칸만 선택한 경우를 선택

    print(max(V[-1]))