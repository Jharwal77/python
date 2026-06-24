age =int(input("Give me your age: "))
day = input("Enter short day: ").lower()

# age = int(input("Give me your age: "))
# day = input("Enter short day: ").lower()

# if age > 18 and (day == "wed" or day == "wednesday"):
#     print("You need to give $10 because today is Wednesday")
# elif age > 18:
#     print("Give $12")
# elif age <= 18 and (day == "wed" or day == "wednesday"):
#     print("You need to give $8 because today is Wednesday")
# else:
#     print("Give $10")

price = 12 if age >= 18 else 10

if day == "wed" or day == "wednesday":
    price -=2

print("you need to give $",price)