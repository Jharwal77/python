file = open('youtube.txt', 'w')

try:
    file.write("Rahul aur python")
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write("Rahul aur Python")