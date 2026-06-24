password = len(input("Enter Your password: "))

if password < 6:
    print("Your password is Weak")
elif password <= 10:
    print("Your password is Medium")
else:
    print("Your password is Strong")