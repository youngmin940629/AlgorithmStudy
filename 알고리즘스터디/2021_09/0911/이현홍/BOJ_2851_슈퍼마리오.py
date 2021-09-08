A = 0

for i in range(10):
    m = int(input())
    if (A - 100)**2 >= (A - 100 + m)**2:
        A += m
    else:
        break
print(A)