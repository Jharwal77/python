n = int(input("Please enter value that you want to check: "))
count = 0
for i in range(1, n+1):
    if i%2 == 0:
        count+=1

print("Even sum is",count)