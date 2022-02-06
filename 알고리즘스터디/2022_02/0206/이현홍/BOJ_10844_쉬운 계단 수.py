N = int(input())
arr = [1] * 10
arr[0] = 0

def circle(arr):
    lst = [0] * 10
    for i in range(10):
        if 0 < i:
            lst[i] += arr[i-1]
        if i < 9:
            lst[i] += arr[i+1]
    return lst

for _ in range(N-1):
    arr = circle(arr)

result = sum(arr)
answer = result % 1000000000
print(answer)