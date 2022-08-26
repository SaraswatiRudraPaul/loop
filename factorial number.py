#write a program to print the factorial of a numbers.
from re import I


a=int(input("enter number"))
factorial=1
while a>=0:
    factorial=factorial*a
    a=a-1
    print(factorial)