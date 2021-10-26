s = 0
H = [0] * 9
for i in range(9):
    H[i] = int(input())
    s += H[i]
H.sort()

t = s - 100
B = 0
for i in range(8):
    for j in range(i+1, 9):
        if H[i] + H[j] == t:
            H[i], H[j], B = -1, -1, 1
            break
    if B: break

for h in H:
    if h > 0: print(h)