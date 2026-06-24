coffee = input("Tell what type(small, medium, and large) you coffee need: ")
option = input("Please, Enter Y/y if you want Extra Shot or N/n if don't want any Extra shot: ")

if (option.lower()) == "y":
    print("Your coffee is",coffee,"with an extra shot")
else:
    print("Your coffee is",coffee)