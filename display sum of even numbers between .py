#Accept two numbers from the user and display sum of even numbers between the (including both).
a=int(input("enter number"))
b=int(input("enter number"))
sum=0
while a<b:
    if a%2==0:
        sum=sum+a
    a=a+1
print(sum)