numbers = []

for i in range(10):
    numbers.append(int(input(f"Enter number {i+1}: ")))

count = 0
for num in numbers:
    if num > 0:
        count+=1
    
print("In given number",count,"numbers is positive")