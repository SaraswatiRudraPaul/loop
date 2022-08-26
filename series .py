#write a program to add frist n terms to the following series using a while loop.1/1!+1/2!+1/3!=...+1/n!.
num=int(input("enter number"))
i=1
while i<=num:
    print("1","/","!","+",end=",")
    i=i+1