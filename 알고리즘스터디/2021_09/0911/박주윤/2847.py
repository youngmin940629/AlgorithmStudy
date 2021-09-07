import sys; sys.stdin = open('2847.txt', 'r')

for tc in range(1,3):
    N = int(input())
    arr = []
    pluss = 0
    for _ in range(N):
        arr.append(int(input()))
    for i in range(N-1):
        if arr[N-i-1] > arr[N-i-2]:
            pass
        else:
            pluss += abs(arr[N-i-2]-arr[N-i-1])
            arr[N-i-2] = arr[N-i-1] - 1
            pluss += 1
    print(pluss)

# 주의할 점 -> i 절대 빼먹지 않기!!!
# 반복문인 점을 잊지 말자