#perfect number
n=int(input("enter the number of perfect number needed:"))
list=[]
count=0
num=1
while count<n:
    sum=0
    num+=1
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        count+=1
        list.append(num)
print(f"first {n}perfect number are {list}")
