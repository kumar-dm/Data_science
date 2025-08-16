#mini calculator

a=int(input("ENTER 1st NUMBER"))
b=int(input("ENTER 2nd number"))
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choice=int(input("ENTER THE CHOICE FROM ABOVE"))
if choice==1:
    print("SUM IS : ",a+b)
elif choice==2:
    print("SUBSTRACTION IS :",a-b)
elif choice==3:
    print("MULTIPLICATION IS :",a*b)
elif choice==4:
    print("DIVISION IS : ",a/b)
else:
    print("INVALID CHOICE")