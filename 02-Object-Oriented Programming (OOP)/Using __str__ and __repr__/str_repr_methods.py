# Define a class named Car to represent a car object
class Car:
    # The constructor (__init__) method initializes the attributes of the Car object
    def __init__(self, make, model, year):
        self.make = make  # The manufacturer of the car (e.g., Toyota, Honda)
        self.model = model  # The model of the car (e.g., Corolla, Civic)
        self.year = year  # The year the car was manufactured

    # The __str__ method is used to define a user-friendly string representation of the object
    # This is typically used for displaying information to end-users
    def __str__(self):
        return f"Car: {self.make} {self.model} ({self.year})"

    # The __repr__ method is used to define a developer-friendly string representation of the object
    # This is typically used for debugging and should ideally return a string that can recreate the object
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

# Create an instance of the Car class
car = Car("Toyota", "Corolla", 2020)

# Print the user-friendly string representation of the car object
# This calls the __str__ method
print(str(car))  # Output: Car: Toyota Corolla (2020)

# Print the developer-friendly string representation of the car object
# This calls the __repr__ method
print(repr(car))  # Output: Car(make='Toyota', model='Corolla', year=2020)
