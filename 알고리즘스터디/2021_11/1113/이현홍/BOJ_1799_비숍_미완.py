import sys; sys.stdin=open('sample.txt', 'r')

N = int(input())

Q=[]
cnt = 0
for r in range(N):
    arr = input().split()
    for c in range(N):
        if arr[c] == '1':
            Q.append((r, c))
            cnt += 1

ans = -1
VL = [1]*(N*2-1)
VR = [1]*(N*2-1)

def bishop(s, n=0):
    global ans
    if s <= ans: return 
    if n == cnt:
        ans = s
        print(ans)
    else:
        bishop(s-1, n+1)
        r = Q[n][0]
        c = Q[n][1]
        if VL[r+c] and VR[r+N-1-c]:
            VL[r+c] = 0
            VR[r+N-c-1] = 0
            bishop(s, n+1)
            VL[r+c] = 1
            VR[r+N-c-1] = 1

bishop(cnt)
print(ans)