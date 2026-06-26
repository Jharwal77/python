class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        # self.total_car +=1
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesal"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electrical"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())
# safari = Car("Tata", "Safari")
# safariThree = Car("Tata", "Nexon")
# print(safari.fuel_type())

# print(safari.total_car)

# print(Car.total_car)

my_car = Car("Tata", "Safari")

# print(my_car.general_description())
print(Car.general_description())