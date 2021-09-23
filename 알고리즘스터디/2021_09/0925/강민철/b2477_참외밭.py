import sys;sys.stdin = open('2477.txt')

K = int(input())
arr = list()

for i in range(6):
    arr.append(list(map(int, input().split())))

idx = -1
while True:
    idx += 1
    idx = idx % 6
    F = [arr[idx][0], arr[(idx+1)%6][0]]
    R = [arr[(idx+2)%6][0], arr[(idx+3)%6][0]]
    if F == R:
        break

sub = arr[(idx+1)%6][1] * arr[(idx+2)%6][1]

width = 0
height = 0
for i in range(6):
    if arr[i][0] <= 2 and arr[i][1] > width:
        width = arr[i][1]
    elif arr[i][0] > 2 and arr[i][1] > height:
        height = arr[i][1]

print((width * height - sub)*K)