n = int(input())
if n*(n+1)%4 == 0:
    b = n*(n+1)//4
    print("YES")
    check = {}
    curr = 0
    for i in range(n,0,-1):
        if b - curr- i >= 0:
            curr+=i
            check[i]=1
        if b-curr - i <0 and b-curr >0:
            check[b-curr]=1
    count = len(check)
    a = [x for x in check]
    b = [x for x in range(1,n+1) if x not in check]
    print(count)
    print(*a)
    print(n-count)
    print(*b)
else:
    print("NO")
