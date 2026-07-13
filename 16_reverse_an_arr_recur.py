
# def reverse(nums,left,right):
#     while left<right:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1
#     return nums
# arr=[1,2,3]
# print(reverse(arr,0,len(arr)-1))

def reverse(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverse(nums,left+1,right-1)
    return nums
arr=[1,2,3]

print(reverse(arr,0,len(arr)-1))