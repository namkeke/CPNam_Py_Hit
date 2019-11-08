def check_add(a, name):
    if name in a:
        a[name] += 1
    else:
        a[name] = 1


a = dict()
for i in range(int(input())):
    b = input()
    check_add(a, b)  
print(max(a.keys(), key=lambda k: a[k]))
