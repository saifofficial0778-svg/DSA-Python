nums1=[1,1,1,2,4,6,7]
nums2=[1,2,2,3,6,7,8,9,10]

m=len(nums1)
n=len(nums2)
i,j=0,0
res=[]

while i < m and j < n:
    if nums1[i]<=nums2[j]:
        if len(res)==0 or res[-1]!=nums1[i]:
            res.append(nums1[i])
        i+=1
    else:
        if len(res)==0 or res[-1]!=nums2[j]:
            res.append(nums2[j])
        j+=1
while i<m:
    if len(res)==0 or res[-1]!=nums1[i]:
        res.append(nums1[i])
    i+=1
while j<n:
    if len(res)==0 or res[-1]!=nums2[j]:
        res.append(nums2[j])
    j+=1
print(res)