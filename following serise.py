#write a program to print the following serise till n terms.2,22,222,2222,.....n terms.
num=int(input("enter number"))
i=1
while i<=num:
    print(i*"2",end=",")
    i=i+1