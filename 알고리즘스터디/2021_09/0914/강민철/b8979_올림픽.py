N, K = map(int, input().split())
arr = list()
for _ in range(N):
    c = list(map(int, input().split()))
    if c[0] == K:
        target = c
    arr.append(c)

cnt = 1
for i in range(N):
    if arr[i][1] > target[1]:
        cnt += 1
    elif arr[i][1] >= target[1] and arr[i][2] > target[2]:
        cnt += 1
    elif arr[i][1] >= target[1] and arr[i][2] >= target[2] and arr[i][3] > target[3]:
        cnt += 1

print(cnt)