
def fun(x,n):
    if n==0:
        return
    print(x)
    fun(x+2,n-1)
    n-=1
fun(2,10)