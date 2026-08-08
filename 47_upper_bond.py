def upper_bond(nums,target):
    low=0
    high=len(nums)-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            high=mid-1
            ub=mid
        else:
            low=mid+1
    return ub
print(upper_bond([1,2,3,3,3,3,4,5],3))