# name = input("Please Enter your name: ")

# def greet(name):
#     if(name == ""):
#         return "guest"
#     else:
#         return name
    
# print("Hey",greet(name),"!")


def greet(name = "guest"):
        return "Hello " + name + "!"
    
print(greet("rahul"))
print(greet())