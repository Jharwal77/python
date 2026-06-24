score = int(input("Please enter 0-100 value: "))

char = "A" if 90 <= score <= 100 else "B" if 80 <= score <= 89 else "C" if 70 <= score <= 79 else "D" if 60<= score <= 69 else "F" 

print("Your grade is: ",char)