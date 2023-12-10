
str=input ("enter the number of elements in the list separated by comma:")
list1=list(map(int,str.split(',')))

print("the list is",list1)
print ("the largest number in the list",max(list1))