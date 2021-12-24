n = int(input())
nums = [int(x) for x in input().split()]
ans = 0
for i in range(n-1):
    if nums[i+1] < nums[i]:
        ans +=nums[i]-nums[i+1]
        nums[i+1] += nums[i]-nums[i+1]
print(ans)
