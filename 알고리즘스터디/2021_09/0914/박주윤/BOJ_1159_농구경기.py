import sys; sys.stdin = open('BOJ_1159_농구경기.txt', 'r')

lst = [0] * 26
for _ in range(int(input())):
    s = input()
    lst[ord(s[0])-97] += 1
for i in range(26):
    if lst[i] >= 5:
        idx = i
        print(chr(idx + 97),end = '')
if max(lst) < 5:
    print('PREDAJA')
