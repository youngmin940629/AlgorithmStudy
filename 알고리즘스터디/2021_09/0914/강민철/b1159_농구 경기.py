N = int(input())
dct = dict()
for i in range(N):
    name = input()
    dct[name[0]] = dct.get(name[0], 0) + 1

lst = list()
for key, val in dct.items():
    if val >= 5:
        lst.append(key)

if lst:
    print(''.join(sorted(lst)))
else:
    print('PREDAJA')