'''
3
5
5
5
'''
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
cnt = 0
for i in range(N-2, -1, -1):
    if data[i] >= data[i+1]:
        while data[i] >= data[i+1]:
            data[i] -= 1
            cnt += 1
print(cnt)