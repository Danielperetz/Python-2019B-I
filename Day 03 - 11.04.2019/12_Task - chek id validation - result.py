while True:
    id=input("Enter your id:")
    if len(id)<=9:
        id="0"*(9-len(id)) + id
        print("you entered id:",id)
        break
    else:
        print("max 9 digits")

sum=0
for i in range(0,len(id)):
    temp=(1+(i%2))*(int)(id[i])
    sum+=temp%10+temp//10

if sum%10==0:
    print ("id is valid")
else:
    print ("id is unvalid")
