#prime number

i=1
co=0
n=int(input("enter the number"))
while i<=n:
    if n%i==0:
        co=co+1
    i=i+1
if co==2:
    print(n," is a Prime NUmber")
else:
    print(n," is a non prime number")