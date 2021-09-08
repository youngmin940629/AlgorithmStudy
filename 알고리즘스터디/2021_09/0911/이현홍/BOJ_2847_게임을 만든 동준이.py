t = int(input())
l = []

for i in range(t):
    l.append(int(input()))
l.reverse()
cnt = 0

for i in range(len(l)-1):
    while l[i] <= l[i+1]:
        l[i+1] -= 1
        cnt += 1

print(cnt)