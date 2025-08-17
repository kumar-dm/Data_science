#program to check palendrome number
n=int(input("Enter The Number"))
rev=0
n1=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==n1:
    print("Palendrome Number")
else:
    print("Not A Palendrome Number")