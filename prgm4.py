#fibinocci
def fun(n):
    if n==0 or n==1:
        return n
    else:
        return fun(n-1)+fun(n-2)
n=int(input("enter the number:"))
print("the fibinocci series is:")
for i in range(n+1):
    print(fun(i),end=" ")