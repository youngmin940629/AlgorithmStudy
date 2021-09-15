# 0부터 w, h로 xy 평면으로 생각
w, h = map(int, input().split())
cut = int(input())
x = [0, w]
y = [0, h]

# 자르겠다고 선언한 수 넣기
for c in range(cut):
    d, l = map(int, input().split())
    if d: x.append(l)
    else: y.append(l)

# 정렬
x.sort()
y.sort()
xd = 0
yd = 0

# 이웃항간에 차이가 가장 큰 수
for i in range(len(x)-1):
    if x[i+1] - x[i] > xd: xd = x[i+1] - x[i]
for j in range(len(y)-1):
    if y[j+1] - y[j] > yd: yd = y[j+1] - y[j]

print(xd * yd)