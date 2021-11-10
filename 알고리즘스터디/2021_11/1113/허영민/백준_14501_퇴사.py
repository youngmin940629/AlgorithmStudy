N = int(input())
day = [0] * (N+1)
work = [0] * (N+1)
for i in range(1,N+1):
    day[i], work[i] = map(int, input().split())
result = 0
def check(n,rst):
    global result
    if result < rst:
        result = rst
    if n > N:
        return
    if n < N+1:
        for i in range(n,N+1):
            if i + day[i] <= N+1:
                check(i+day[i], rst+work[i])
    check(n+1, rst)


check(1,0)
print(result)