n=1234
num=n
result=0
while num>0:
    ld=num%10
    num=num//10
    result=result*10+ld
if result==n:
    print(1) 
else:
    print(0)  
print(result)
    
    
    