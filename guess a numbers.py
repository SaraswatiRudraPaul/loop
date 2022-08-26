#write a python program to guess a numbers  between 1to9.
i=1
a=int(input("enter numbers"))
while i<=a:
    b=int(input("enter numbers"))
    i=i+1
    if b==a:
        print("you a guess right")
        break
    else:
        print("you guess right")
        