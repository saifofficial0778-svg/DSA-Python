

# def palindrom(s):
#     s=list(s)
#     left=0
#     right=len(s)-1
#     while left < right:
#         if s[left]!=s[right]:
#             return False
        
#         left+=1
#         right-=1
#     return True

# print(palindrom("nitin"))

def palindrom(s,left,right):
    s=list(s)
    
    if left >= right:
        return True
    if s[left]!=s[right]:
        return False
    
    return palindrom(s,left+1,right-1)
     
str="fhyfweiugw"    
print(palindrom(str,0,len(str)-1))
        