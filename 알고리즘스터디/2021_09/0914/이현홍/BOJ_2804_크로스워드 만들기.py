# a = 가로 단어,  b = 세로 단어
a,b = input().split()

ida = -1
idb = -1

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            ida = i
            idb = j
            break
    if ida != -1:
        break

for k in range(len(b)):
    if k == idb:
        print(a)
    else:
        print('{}{}{}'.format('.'*ida, b[k], '.'*(len(a)-ida-1)))