n = int(input())
def sum_odd(n):
    return n*(n-1)+1
for i in range(n):
    a,b = map(int,input().split())
    d = max(a,b)
    c = sum_odd(d)
    if d%2 == 0:
        print(c+a-b)
    else:
        print(c+b-a)
