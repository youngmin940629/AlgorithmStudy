lst = list()
for i in range(10):
    lst.append(int(input()))

tot = 0
for i in range(10):
    if abs(tot-100) >= abs(tot + lst[i] - 100):
        tot += lst[i]
    else:
        break
print(tot)