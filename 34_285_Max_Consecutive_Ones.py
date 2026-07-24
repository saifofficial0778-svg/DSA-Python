def findMaxConsecutiveOnes(nums):
        max_count=0
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                count+=1
            else:
                count=0
            max_count=max(max_count,count)
        return max_count

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))