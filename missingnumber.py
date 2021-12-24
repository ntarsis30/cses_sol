num = int(input())
nums = list(map(int, input().split()))
print(num*(num+1)//2- sum(nums))
