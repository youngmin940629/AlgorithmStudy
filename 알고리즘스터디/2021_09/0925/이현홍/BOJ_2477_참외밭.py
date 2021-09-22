K = int(input())
dir = [0] * 6
l = [0] * 6
l_box = 0
s_box = 0

for i in range(6):
    dir[i], l[i] = map(int, input().split())

dir += dir
l += l

for k in range(2, len(dir)-3):
    if dir[k-1] == dir[k+1] and dir[k-2] == dir[k]:
        l_box = l[k+2] * l[k+3]
        s_box = l[k-1] * l[k]

print(K * (l_box - s_box))