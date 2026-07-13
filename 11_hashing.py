n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
mydict={}
for i in range(0,len(m)):
    count=0
    for j in range(0,len(n)):
        if m[i]==n[j]:
            count+=1
    mydict[m[i]]=count
print(mydict)