nums=[1,2,3,4,4,4,4,5,6]
target=4
n=len(nums)
first=-1
last=-1
for i in range(n):
    if nums[i]==target:
        if first==-1:
            first=i
        last=i
print(last-first+1)