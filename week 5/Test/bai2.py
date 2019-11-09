import random

n = 6
a = [5, 6, 7, 2, 1, 3]
b = []
c = []
d = round(n/3)

for i in range(d):
    ii = random.randint(0, 6)
    b.append(a[ii])
    a.pop(ii)
print(b)
print(a)
