n=int(input("enter the number n: "))
nod=len(str(n))
result=0
num=n

while num>0:
    ld=num%10
    num=num//10
    result=result+ld**nod
    
if(result==n):
    print(1)
else:
    print(0)