def check(a):
    t = a
    s = 0
    while(a != 0):
        r = a % 10
        s = s*10+r
        a /= 10
    if t == s:
        return 1
    return 0


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if check(a[i]) == 1:
        print(i)
