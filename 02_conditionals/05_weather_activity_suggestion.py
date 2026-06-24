weather = input("Please enter weather is sunny, rainy, or snowy: ")

activity = "Go for a Walk" if weather.lower() == "sunny" else "Read a Book" if weather.lower() == "rainy" else "Build a Snowman" if weather.lower() == "snowy" else "Do what you want ?"

print("You need to do this :",activity)