#write a program to find the sum of the following serrise.1+2+6+24+120....n terms.
num=int(input("enter number"))
i=1
a=1
sum=0
while i<=num:
    a=i*a
    sum=a+sum
    i=i+1
print(sum)
