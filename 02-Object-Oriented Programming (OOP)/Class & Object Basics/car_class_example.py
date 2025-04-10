class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"     

car1 = car("Toyota", "Corolla", 2020)
car2 = car("Honda", "Civic", 2019)
car3 = car("Ford", "Mustang", 2021)
car4 = car("Chevrolet", "Camaro", 2022)
car5 = car("Nissan", "Altima", 2023)    
print(car1.display_info())
print(car2.display_info())
print(car3.display_info())
print(car4.display_info())
print(car5.display_info())
