def subsets(nums,target):
    result = []
    subset=[]

    def solve(i):
        if i == len(nums):
            if sum(subset)==target:
                result.append(subset.copy())
            return

        subset.append(nums[i])
        solve(i + 1)

        subset.pop()

        solve(i + 1)

    solve(0)
    return result

print(subsets([5,9,4,3,1], 9))