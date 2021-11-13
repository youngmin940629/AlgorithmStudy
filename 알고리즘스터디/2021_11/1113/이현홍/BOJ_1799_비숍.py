import sys; sys.stdin=open('sample.txt', 'r')
# 
# 0 1 0 1   0번 칸과 1번 칸은 서로에게 영향을 주지 않는다.
# 1 0 1 0   두 영역으로 나누어 계산하면 속도가 훨씬 빠르다.
# 0 1 0 1
# 1 0 1 0

N = int(input())
# 칸 분리해서 담기
Q0, Q1 = [], []
for r in range(N):
    s = input().split()
    for c in range(N):
        if s[c] == '1':
            if (r+c)%2: Q0.append((r, c))
            else:Q1.append((r, c))

# 분리해서 답 구하기
ans0, ans1 = -1, -1
l0, l1 = len(Q0), len(Q1)
VR, VL = [1]*(N*2-1), [1]*(N*2-1)

def bishop(s, k, n=0):
    G = 0
    # 분리 배정
    global ans0, ans1, l0, l1
    if k == 0:
        ans, Q, l = ans0, Q0, l0
    elif k == 1:
        ans, Q, l = ans1, Q1, l1
    # 가능한 답이 현재 답보다 작으면 중단
    if s < ans: return
    # 끝까지 도달하면
    if n == l:
        # 한 번 더 답 확인해서 크면 변경
        if ans < s:
            if k == 0: ans0 = s
            else: ans1 = s
    else:
        a, b = Q[n]
        G = 1   # 진행 여부
    if G:
        r, c= a+b, a+N-1-b
        # 대각선 유무 확인
        if VR[r] and VL[c]:
            VR[r], VL[c] = 0, 0
            # 비숍 놓고 진행
            bishop(s, k, n+1)
            VR[r], VL[c] = 1, 1
        # 안 놓고 진행은 무조건 진행
        bishop(s-1, k, n+1)

bishop(l0, 0), bishop(l1, 1)
print(ans0 + ans1)