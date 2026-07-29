def transpose(nums):
    rows=len(nums)
    cols=len(nums[0])
    res=[[0]*rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            res[j][i]=nums[i][j]
    return res
arr=[[5,9,1],[2,3,7]]
print(transpose(arr))