nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)

# # [10] + [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums[:] = [nums[n - 1]] + nums[0 : n - 1]

# print(nums)  # Output: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp

print(nums)