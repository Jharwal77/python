fruit_name = input("Enter fruit name: ")
fruit_color = input("Enter your fruit color: ")

result = "unripe" if fruit_color.lower() == "green" else "ripe" if fruit_color.lower() == "yellow" else "overripe" if fruit_color.lower() == "brown" else "not know"

print("Your ",fruit_name,"is",result)