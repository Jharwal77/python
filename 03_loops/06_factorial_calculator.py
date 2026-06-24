value = int(input("Please Enter number: "))
fac = 1
# i=1
# while i <= value:
#     fac = i*fac
#     i+=1

# print("Factorial of",value,"is",fac)

while value > 0:
    fac = fac*value
    value-=1

print("Your factorial is",fac)