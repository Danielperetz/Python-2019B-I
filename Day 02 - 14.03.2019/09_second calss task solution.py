num=int(input("Enter your number: "))
arr=["zero","one","two","three","four","five","six","seven","eight","nine"]

if num>=1000:
    print("Num is more than 3 digits", num)
elif num < 10:
    print(arr[num])
elif num < 100:
    digit1=num%10
    digit2=num//10
    print("Num is 2 digits", num, "sum is: " , digit1+digit2)
else:
    digit1=num%10
    digit2=num//10%10
    digit3=num//100
    print("Num is 3 digits", num, "mul is: " , digit1*digit2*digit3)

