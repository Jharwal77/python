items = ["apple", "banana", "orange", "apple", "mango"]

# for i in items:
#     if (items.count(i)) == 1:
#         continue
#     else:
#         print("Find duplicate and that is",i)
#         break

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ",item)
        break
    unique_items.add(item)