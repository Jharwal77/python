pet = input("Enter pet species (dog/cat): ").lower()
age = int(input("Enter pet age: "))

if pet == "dog":
    if age < 2:
        print("Recommended food: Puppy food")
    else:
        print("Recommended food: Adult dog food")

elif pet == "cat":
    if age > 5:
        print("Recommended food: Senior cat food")
    else:
        print("Recommended food: Adult cat food")

else:
    print("Unknown pet species")