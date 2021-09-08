import sys
sys.stdin = open('2851.txt', 'r')

sol = 0
max1 = max2 = 0
for i in range(10):
    data = int(input())
    if data == 100:
        sol = 100
        break
    else:
        sol += data
        if sol > 100:
            max1 = sol - 100
            max2 = 100 - (sol - data)
            break
if max1 == max2:
    print(sol)
elif max1 > max2:
    print(sol - data)
elif max1 < max2:
    print(sol)



