n=int(input("Enter a number:"))
flag=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        flag=False
if flag:
    print("Given number is prime")
else:
    print("Given number is not prime")