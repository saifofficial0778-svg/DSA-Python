nums=[5,3,9,8,1,6,4,-10,-100]
nums2=[10,20,25,10,10,-5,-3,-2,7]


def liner_search(nums,target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
    return -1
        
print(liner_search(nums2,100))
        