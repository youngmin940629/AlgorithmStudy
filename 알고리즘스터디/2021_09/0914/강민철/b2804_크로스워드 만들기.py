import sys;sys.stdin = open('2804.txt')

A, B = input().split()

for i in range(len(A)):
    flag = 0
    for j in range(len(B)):
        if A[i] == B[j]:
            idx_A = i
            idx_B = j
            flag = 1
            break
    if flag:
        break

for i in range(len(B)):
    for j in range(len(A)):
        if i == idx_B:
            print(A[j], end = '')
        elif j == idx_A:
            print(B[i], end = '')
        else:
            print('.', end='')
    print()