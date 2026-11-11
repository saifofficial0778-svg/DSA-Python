def subsets(nums):
    result = []
    subset=[]

    def solve(i):
        if i == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        solve(i + 1)

        subset.pop()

        solve(i + 1)

    solve(0)
    return result

print(subsets([2,4,6]))