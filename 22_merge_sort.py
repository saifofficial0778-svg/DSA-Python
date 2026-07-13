def merge_arr(left,right):
     i,j=0,0
     result=[]
     n,m=len(left),len(right)
     
     while i<n and j<m:
        if left[i]<=right[j]:
             result.append(left[i])
             i+=1
        else:
            result.append(right[j])
            j+=1
     if i<n:
        while i<n:
            result.append(left[i])
            i+=1
     if j<m:
        while j<m:
            result.append(right[j])
            j+=1
     return result


def merge_sort(arr):
     if len(arr)<=1:
          return arr
     mid =len(arr)//2
     left_half=arr[:mid]
     right_half=arr[mid:]
     left=merge_sort(left_half)
     right=merge_sort(right_half)
     return merge_arr(left,right)

arr1=[3,1,2,4,5,6,9]

print(merge_sort(arr1))
     