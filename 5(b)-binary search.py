print("20CS241_ISHITA G")
data=[]
n=int(input("Enter the number of elements in the array:"))
print("Enter the elements in an Ascending order !")
for i in range(0,n):
      x = int(input("Enter the element %d :"%(i+1)))
      data.append(x)
e=int(input("Enter the element to be searched :"))
first=0
last=n-1
found=False
while(first<=last and not found):
    mid=(first+last)//2
    if data[mid]==e:
        found=True
    else:
        if e<data[mid]:
            last=mid-1
        else:
            first=mid+1
if found:
    print("Element",e,"found at the position",mid+1,".")
else:
    print("Element",e,"NOT found in the array!")
