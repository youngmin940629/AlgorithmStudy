N = int(input())
Q = list(map(int, input().split()))
tools = list(map(int, input().split()))

mx = -10000000000000  #음수, 범위 주의
mn = 10000000000000
def sc(n=0, s=0):
    if n == N:
        global mx, mn
        if s > mx: mx = s
        if s < mn: mn = s
    else:
        if n == 0:
            s = Q[0]
            sc(n+1, s)
        else:
            for i in range(4):
                if tools[i]:        # 연산자가 남았으면
                    tools[i] -= 1   # 하나 소모하고
                    if i == 0:
                        ns = s + Q[n]
                    elif i == 1:
                        ns = s - Q[n]
                    elif i == 2:
                        ns = s * Q[n]
                    elif i == 3:
                        if s < 0: ns = -(abs(s) // Q[n])
                        else: ns = s//Q[n]
                    sc(n+1, ns)     # 계산값 전달, 다음 숫자 재귀
                    tools[i] += 1   # 연산자 다시 회복, 완전탐색
sc()

print(mx)
print(mn)
