flag=False

while not flag:
    num=input("enter a number: ")
    flag=True

    index=0 
    times_to_check=len(num)//2

    while index < times_to_check:
        flag=flag and num[index] == num[len(num)-1-index]
        index+=1
        
    if flag:
        print(num, "is polindrom")
