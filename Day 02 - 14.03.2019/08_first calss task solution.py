num=int(input("Enter your number: "))

if num>=1000:
    print("Num is more than 3 digits", num)
elif num < 10:
    if num==0:
        print("zero")
    elif num==1:
        print("one")    
    elif num==2:
        print("two")    
    elif num==3:
        print("three")    
    elif num==4:
        print("four")    
    elif num==5:
        print("five")    
    elif num==6:
        print("six")    
    elif num==7:
        print("seven")    
    elif num==8:
        print("eight")
    elif num==9:
        print("nine")

elif num < 100:
    digit1=num%10
    digit2=num//10
    print("Num is 2 digits", num, "sum is: " , digit1+digit2)
else:
    digit1=num%10
    digit2=num//10%10
    digit3=num//100
    print("Num is 3 digits", num, "mul is: " , digit1*digit2*digit3)

