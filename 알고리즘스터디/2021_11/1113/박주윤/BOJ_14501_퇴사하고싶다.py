import sys; sys.stdin = open('BOJ_14501_퇴사하고싶다.txt', 'r')
n = int(input())

t = [0]
p = [0]
d = [0] * (n+2)
result = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(1, n+2):
    for j in range(1, i):
        d[i] = max(d[i], d[j])

        if j + t[j] == i:
            d[i] = max(d[i], d[j] + p[j])

    result = max(result, d[i])

print(result)