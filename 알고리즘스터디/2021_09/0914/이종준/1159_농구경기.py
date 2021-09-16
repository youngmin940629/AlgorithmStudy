'''
18
babic
keksic
boric
bukic
sarmic
balic
kruzic
hrenovkic
beslic
boksic
krafnic
pecivic
klavirkovic
kukumaric
sunkic
kolacic
kovacic
prijestolonasljednikovi
'''

N = int(input())

first_chrs = []

for i in range(N):
    first_chrs.append(input()[0])
first_chrs.sort()
cnt = 1
my_string = ''

for i in range(N-1):
    if first_chrs[i] in my_string:
        continue
    elif first_chrs[i] == first_chrs[i+1]:
        cnt += 1
        if cnt == 5:
            my_string += first_chrs[i]
            cnt = 1
    else:
        cnt = 1

if not my_string:
    print('PREDAJA')
else:
    print(my_string)