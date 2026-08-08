def lower_bond(nums,target):
    low=0
    high=len(nums)-1
    lb=len(nums)
    while low<=high:
        mid=(low+high)//2
        
        if nums[mid]>=target:
            high=mid-1
            lb=mid
        else:
            low=mid+1
    return lb
print(lower_bond([1,2,3,3,3,3,4,5],3))