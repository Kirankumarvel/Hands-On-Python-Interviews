# #Polymorphism	Method overriding using base and derived class
# ✅ . Polymorphism with Method Overriding
# Q: Show how method overriding works between base and derived classes.
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

a = Animal()
d = Dog()
print("Animal: " + a.speak())  # Output: Animal speaks
print("Dog: " + d.speak())     # Output: Dog barks
