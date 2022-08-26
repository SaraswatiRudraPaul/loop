#write a program to accept 10 numbers from the user and display it's average.
i=1
sum=0
while i<=10:
    num=int(input("enter number"))
    sum=sum+num
    i=i+1
print(sum)
avg=sum/10
print(avg)