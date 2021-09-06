data = []
N = int(input())
cnt = 0
for tc in range(0, N):
    data = data + [int(input())]
for idx in range(N - 1, 0, -1):
    while data[idx] <= data[idx - 1]:
        if data[idx] <= data[idx - 1]:
            data[idx - 1] -= 1
            cnt += 1
print(cnt)