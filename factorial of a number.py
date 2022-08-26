#write a program to print the factorial of a number accepted by the user.
num=int(input("enter number"))
factorial=1
i=1
while i<=num:
    factorial=factorial*i 
    i=i+1
print("factorial=",factorial)
