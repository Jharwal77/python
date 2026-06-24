distance = int(input("Please Enter your distance in K/M: "))

mode = "Walk" if distance < 3 else "Bike" if 3<= distance <=15 else "Car" if distance >15 else "This is out of the box value or selection"

print("I suggest you please go for",mode)