def matrix(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if i+j==2:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()
arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix(arr)
    