# program to check armstrong number




n=int(input("enter a number"))
s=0
n1=n
while n>0:
    rem=n%10
    s=s+rem**3
    n=n//10
if s==n1:
     print("Armstrong Number")
else:
    print(" not a armstrong number")