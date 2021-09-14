import sys
sys.stdin = open('2804.txt', 'r')

A, B = input().split()
N, M = len(A), len(B)

for i in range(N):
    if A[i] in B:
        idx = i
        w = B.index(A[i])
        break

for j in range(M):
    if j == w:
        print(A)
    else:
        print('.' * idx + B[j] + '.' * (N-idx-1))

