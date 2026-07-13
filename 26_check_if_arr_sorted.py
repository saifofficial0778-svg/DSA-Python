nums=[1,2,3,5,8,3,10,14,15]
nums1=[3,5,6,8,9,10,20]
def check_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(check_sorted(nums1))