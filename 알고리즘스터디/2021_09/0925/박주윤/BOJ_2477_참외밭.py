import sys; sys.stdin = open('BOJ_2477_참외밭.txt', 'r')

ak = int(input())
fl = []
bl = []

for _ in range(6):
    n, m = map(int, input().split())
    fl.append(n)
    bl.append(m)
for i in range(6):
    if fl[i] == fl[(i+2) % 6] and fl[(i+1) % 6] == fl[(i+3) % 6]:
        idx = i
print(ak*(bl[(idx + 4) % 6]*bl[(idx + 5) % 6]-bl[(idx + 1) % 6]*bl[(idx + 2) % 6]))