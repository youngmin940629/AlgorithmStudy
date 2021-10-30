import sys;sys.stdin = open('2309.txt')

height = list()
for _ in range(9):
    height.append(int(input()))
height.sort()
ans = [0] * 7

def search(n, m, s, k, sumation):
    if sumation > 100:
        return
    if k == m:
        if sumation == 100:
            return 1
    else:
        for i in range(s, n-m+1+k):
            ans[k] = height[i]
            sumation += height[i]
            if search(n, m, i+1, k+1, sumation):
                return 1
            sumation -= height[i]

search(9, 7, 0, 0, 0)
for i in range(7):
    print(ans[i])