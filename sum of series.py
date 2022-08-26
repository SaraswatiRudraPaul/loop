#write a program to find the sum of folowing series 1+8+27.....n terms.
num=int(input("enter number"))
i=1
sum=0
while i<=num:
    print(i**3,"+",end=" ")
    i=i+1
print(sum)