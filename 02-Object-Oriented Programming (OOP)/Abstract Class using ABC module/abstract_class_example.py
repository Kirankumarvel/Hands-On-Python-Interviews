# #	Abstract Classes	Shape abstract class with Rectangle subclass
# ✅ 6. Abstract Class using ABC module
# Q: Define an abstract class Shape and implement it in Rectangle.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r = Rectangle(5, 10)
print(f"Area of rectangle: {r.area()}")  # Output: Area of rectangle: 50
# ✅ 7. Abstract Class using ABC module with Circle subclass 
