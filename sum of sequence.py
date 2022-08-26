#write a python program to sum of the sequence.1+1/1!+1/2!+1/3!+...+1/n!.
num=int(input("enter number"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print("1","/",sum,"!","+")