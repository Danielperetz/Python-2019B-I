flag=False

while not flag:
    num=input("enter a number: ")
    cnt=0
    flag=True
    while cnt < len(num)//2:
        flag=flag and num[cnt] == num[len(num)-1-cnt]
        cnt+=1
    if flag:
        print(num, "is polindrom")
