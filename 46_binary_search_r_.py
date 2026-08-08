def binary_search_r(nums,low,high,target):
    if low>high:
        return -1
    mid = (low + high) // 2
    if nums[mid] > target:
        return binary_search_r(nums, low, mid - 1, target)
    elif nums[mid] < target:
        return binary_search_r(nums, mid + 1, high, target)
    else:
        return True
print(binary_search_r([1,2,3,4,5],0,4,5))
