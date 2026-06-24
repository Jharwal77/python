# def print_kwargs(name, power):
#     print("Name:",name,"power:",power)

# print_kwargs(name="Rahul", power = "lazer")

# def print_kwargs(name, power):
#     print("Name:",name,"power:",power)

# print_kwargs(power = "lazer", name="Rahul")


def print_kwargs( **kwargs ):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(power = "lazer", name="Rahul", enemy = "Dr balal dev")