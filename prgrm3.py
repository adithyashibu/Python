#binary search
str=input("enter the element into the list in sorted order separated by commas:")
list1=list(map(int,str.split(',')))
flag=False
print(f"list:{list1}")
key=int(input("enter the element to be serached:"))
low=0
high=len(list1)-1
while low<=high:
    mid=(low+high)//2
    if list1[mid]==key:
        print(f"element found at the index{mid}")
        flag=True
        break
    elif list1[mid]>key:
        high=mid-1
    else:
        low=mid+1

if not flag:
    print("element is not found in the list")

