#write a program to display sum of odd numbers and even numbers separetly that fall between two numbers accepted from user.(including both numbers)100and500.
a=int(input("enter number"))
b=int(input("enter number"))
s=0
p=0
while a<=b:
    if a%2==0:
        s=s+a
    elif a%2==1:
        p=p+a
    a=a+1
print("even num=",s)
print("odd num=",p)