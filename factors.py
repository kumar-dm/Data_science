#factors or divisors


n=int(input("Enter the Number"))
i=1
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i=i+1