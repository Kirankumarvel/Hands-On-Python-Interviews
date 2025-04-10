#Inheritance + super()	Vehicle and Bike class using super()
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.type_of_bike = type_of_bike

    def details(self):
        return f"Bike Brand: {self.brand}, Model: {self.model}, Type: {self.type_of_bike}"  
    
b = Bike("Yamaha", "YZF-R3", "Sport")
print(b.details())  # Output: Bike Brand: Yamaha, Model: YZF-R3, Type: Sport    
