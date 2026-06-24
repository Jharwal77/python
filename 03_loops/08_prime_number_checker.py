num = int(input("Please Enter your number that you want to check, it is prime or not: "))

is_prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
        

if (is_prime == True):
    print("Your",num,"is prime number")
else:
    print("Your",num,"is not prime number")