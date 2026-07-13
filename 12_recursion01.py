count=0
# def fun():
#     global count
#     if count==4:
#         return
#     print("saif")
#     count+=1
#     fun()
# fun()

def func():
    global count
    if count==4:
        return
    count+=1
    func()
    print("saif")
func()
    
    