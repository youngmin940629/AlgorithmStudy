import sys; sys.stdin = open('BOJ_2309_일곱난쟁이.txt', 'r')

arr = list(int(input()) for _ in range(9))
key = sum(arr)-100
flag = 0
for i in range(8):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == key:
            idx_1 = i
            idx_2 = j
            flag = 1
            break
    if flag == 1:
        break
s = []
for i in range(idx_1):
    s.append(arr[i])
for i in range(idx_1 + 1, idx_2):
    s.append(arr[i])
for i in range(idx_2 + 1, 9):
    s.append(arr[i])
s.sort()
for i in range(7):
    print(s[i])