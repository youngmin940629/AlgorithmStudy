n = int(input())
lst = list(map(int, input().split()))

max_uphill = 0
uphill = 0
for i in range(1, n):
    if lst[i] > lst[i-1]:
        uphill += lst[i] - lst[i-1]
        if uphill > max_uphill:
            max_uphill = uphill
    else:
        uphill = 0
print(max_uphill)