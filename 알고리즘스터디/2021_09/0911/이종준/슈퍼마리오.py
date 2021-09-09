'''
10
20
30
40
50
60
70
80
90
100
'''
data = []
for _ in range(10):
    data.append(int(input()))
result = 0
my_sum = 0
for i in range(10):
    my_sum += data[i]
    if my_sum >= 100:
        prev_sum = my_sum - data[i]
        if my_sum - 100 > 100 - prev_sum:
            result = prev_sum
        else:
            result = my_sum
        break
if my_sum < 100:
    print(my_sum)
else:
    print(result)

