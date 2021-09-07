import sys; sys.stdin = open('슈퍼마리오.txt', 'r')
arr = []
arr1 = []
arr2 = []
ans = 0
cnt = 0

for _ in range(10):
    arr1.append(int(input()))

for i in range(len(arr1)):
    ans += arr1[i]
    arr.append(ans)
    arr2.append(abs(ans - 100))

for i in range(len(arr2)-1):
    if arr2[i] >= arr2[i+1]:
        cnt += 1
print(arr[cnt])