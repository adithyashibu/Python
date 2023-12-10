n = int(input("enter the number:"))
flag = False

for i in range(2,n):
    if n % i == 0:
        flag = True
        break

if flag:
    print("it is not a prime") 
else:
    print("it is a prime")