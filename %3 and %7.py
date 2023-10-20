i = int(input("enter your number : "))
if i%3==0 and i%7==0:
    while i<=1000:
        i+=1
        if i % 3 == 0 and i % 7 == 0:
            print(i)
else:
    print("sorry!")