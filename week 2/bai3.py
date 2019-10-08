num = int(input())
for i in range(1, num+1): print(str(i)+"," if int(i**0.5)**2==i else '',end='')