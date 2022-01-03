n = int(input())
for i in range(1,n+1):
    j = i**2
    a = j*(j-1)//2
    print(a-4*(i-1)*(i-2))
