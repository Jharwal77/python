year = int(input("Please enter year: "))

if (year%4 ==0 and year%100 ==0 and year%400 == 0):
    print(year,"Is Leap Year")
else:
    print(year,"Is not a Leap Year")