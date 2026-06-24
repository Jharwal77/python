# num = int(input("Please Enter number tiil i get 1-10 number: "))

# while not(1<= num <=10):
#     num = int(input("Please Enter number tiil i get 1-10 number: "))

# print("Thanks i got my number that b/w 1-10:",num)

while True:
    num = int(input("Please Enter number that belong to b/w 1-10: "))
    if 1<= num <= 10:
        print("Thanks i got my number that b/w 1-10:",num)
        break
    else:
        print("Please Enter valid number that belong to b/w 1-10: ")