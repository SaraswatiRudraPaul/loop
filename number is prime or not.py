#write a program to check wheather a number is prime or not.
a=int(input("enter number"))
i=2
while i<=a//2:
    if a%i==0:
        print("it is not a prime number")
        break
    i+=1
else:
    print("it is prime number")