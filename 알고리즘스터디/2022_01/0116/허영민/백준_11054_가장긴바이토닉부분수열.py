S = int(input())
arr = list(map(int, input().split()))
dpup = [0] * S
dpdown = [0] * S
result = [0] * S
for i in range(S):
    for j in range(i):
        if arr[i] > arr[j] and dpup[i] < dpup[j]:
            dpup[i] = dpup[j]
    dpup[i] += 1
for i in range(S-1, -1, -1):
    for j in range(S-1, i, -1):
        if arr[i] > arr[j] and dpdown[i] < dpdown[j]:
            dpdown[i] = dpdown[j]
    dpdown[i] += 1
for i in range(S):
    result[i] = dpup[i] + dpdown[i] - 1
print(max(result))