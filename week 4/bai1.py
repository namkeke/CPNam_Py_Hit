def add(a, b):
    return a+b


a, b = list(map(int, input().split())), list(map(int, input().split()))
for i in range(min(len(a), len(b))):
    print(add(a[i], b[i]), end=' ')
if len(a) < len(b):
    for i in range(len(a), len(b)):
        print(b[i])
if len(b) < len(a):
    for i in range(len(b)-len(a)):
        print(a[i])
