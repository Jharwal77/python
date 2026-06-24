value = input("Please Enter any char that you want to check: ")

for char in value:
    if value.count(char) == 1:
        print("This is come only one time:",char)
        break