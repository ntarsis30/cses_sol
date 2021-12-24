c = int(input())
b = [c]
while c > 1:
    if c%2 == 0:
        b.append(int(c//2))
        c //= 2
    else:
        b.append(int(c*3+1))
        c = int(c*3+1)
print(*b)
