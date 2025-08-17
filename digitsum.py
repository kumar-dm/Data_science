#sum of digit of a number

n=int(input("enter the number "))
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
print("The sum is ",s)