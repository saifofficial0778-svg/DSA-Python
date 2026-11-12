def subsets(nums,target):
    result = []
    subset=[]

    def solve(i,total):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target or i==len(nums):
            return 

        subset.append(nums[i])
        total+=nums[i]
        
        solve(i + 1,total)
        
        subset.pop()
        total-=nums[i]

        solve(i + 1,total)

    solve(0,0)
    return result

print(subsets([5,4,9,3,1],9))