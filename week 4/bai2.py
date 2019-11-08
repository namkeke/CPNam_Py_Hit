def check(a, b):
    for i in a:
        if i in b:
            print(i, end=' ')


a, b = set(map(int, input().split())), set(map(int, input().split()))
check(a, b)
