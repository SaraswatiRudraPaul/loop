#write a program to display all even numbers that fall between two numbers(exclusive both numbers)entered by the user.
num=int(input("enter a number"))
i=1
while i<num:
    if i%2==0:
        print(i)
    i+=1