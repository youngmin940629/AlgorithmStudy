import sys;sys.stdin = open('1003.txt')

zero = [1, 0] + [0]*39
one = [0, 1] + [0]*39

for i in range(2, 41):
    zero[i] = zero[i-2] + zero[i-1]
    one[i] = one[i-2] + one[i-1]

for tc in range(int(input())):
    N = int(input())
    print(zero[N], one[N])