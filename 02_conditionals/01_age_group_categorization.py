age = input("Give me your age: ")

age_int = int(age)

if age_int < 13:
    print("Child")

elif age_int < 20:
    print("Teenage")

elif age_int < 59:
    print("Adult")

else:
    print("Senior")