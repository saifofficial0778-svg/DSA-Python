n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
mydict={}
for  i in range(0,len(n)):
    if n[i] in mydict:
        mydict[n[i]]+=1
    else:
        mydict[n[i]]=1
for i in range(0,len(m)):
    print(mydict.get(m[i],0))
    