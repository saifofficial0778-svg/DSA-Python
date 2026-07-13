n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
mylist=[0]*11
for i in range(0,len(n)):
    mylist[n[i]]+=1
# print(mylist)

for i in range(0,len(m)):
    if m[i]>10 or m[i]<1:
        print(0)
    else:
        print(mylist[m[i]])