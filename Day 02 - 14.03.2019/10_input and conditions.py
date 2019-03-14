
day=int(input("Enter day (1-7) : "))
month=int(input("Enter month (1-12) : "))

dayList=["Sun","Mon","Tue","Wen","Thu","Fri","Sat"]
monthList=["January","February","March","April","May","June","July","August","September","October","November","December"]

if day>=1 and day<=7 and month>=1 and month<=12:
    print(dayList[day-1],"/",monthList[month-1])
else:
    print("Invalid input")


"""
Example 1 of program execution:
___________________________________
Enter day (1-7) : 1
Enter month (1-12) : 1
Sun / January


Example 2 of program execution:
___________________________________
Enter day (1-7) : 9
Enter month (1-12) : 3
Invalid input
"""
