def floor_ciel(nums,target):
    low=0
    n=len(nums)
    high=n-1
    ciel=-1
    floor=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            high=mid-1
            ciel=nums[mid]
        else:
            low=mid+1
            floor=nums[mid]
    return [floor,ciel]

print(floor_ciel([1,2,4,5],3))