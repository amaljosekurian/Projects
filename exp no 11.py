x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
z=int(input("Enter the number: "))
if(x>y) and (x>z):
    print("The greatest number is: ",x)
elif(y>z):
    print("The greatest number is: ",y)
else:
    print("The greatest number is: ",z)