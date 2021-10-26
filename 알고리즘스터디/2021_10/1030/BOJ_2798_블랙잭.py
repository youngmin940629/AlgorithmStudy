def slt(x=0, n=3, s=0):
    global answer
    if n == 0:
        if answer < s <= M:
            answer = s 
    else:
        for i in range(x, N+1-n):
            if s+L[i] <= M:
                slt(i+1, n-1, s+L[i])
N, M = map(int, input().split())
L = tuple(map(int, input().split()))
answer = 0
slt()
print(answer)