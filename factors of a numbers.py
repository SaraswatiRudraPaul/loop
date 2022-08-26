#write a program to print all the factors of a numbers using a while loop.
from re import I


num=int(input("enter number"))
fac=1
i=1
while i<=num:
    fac=fac*i 
    print(fac)
    i=i+1