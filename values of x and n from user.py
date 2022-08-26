#write a program to print the sum of the following serise (accepted values of x and n from user)
#1+X/1!+X2/2!+.....Xn/n!.
#x+x2/2+....xn/n.
x=int(input("enter number"))
n=int(input("enter nummber"))
i=0
print(i,end=",")
while i<n:
    print("+","x",i,"/",i,"!",end="")
    i=i+1