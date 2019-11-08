a, b = list(map(int, input().split())), list(map(int, input().split()))
Sa = abs((a[0]-a[2])*(a[1]-a[3]))
Sb = abs((b[0]-b[2])*(b[1]-b[3]))
if a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1]:
    print(Sa+Sb)
else:
    Sab = (min(a[2], b[2]) - max(a[0], b[0])) * \
        (min(a[3], b[3]) - max(a[1], b[1]))
    print(Sa+Sb-2*Sab)

