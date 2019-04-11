while True:
    num=(int)(input("Enter num: "))
    original_num=num
    temp=0

    while num!=0:
        temp=temp*10+num%10
        num//=10
    if original_num==temp:
        print(original_num, "is polindrom")
        break
