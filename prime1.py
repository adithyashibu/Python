list1=[]
str=(input("enter the elements in the list separated by comma:"))
list1=list(map(int,str.split(",")))
print("the list is ",list1)

prime=[]
for i in list1:
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
            prime.append(i)
print("prime numbers are :",prime)         

