value = input("Please Enter any string that you want to reverse? : ")


rev_str =''
for char in value:
    rev_str = char + rev_str

print("This is my reverse string :",rev_str)