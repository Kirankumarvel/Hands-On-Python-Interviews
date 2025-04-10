#Multiple Inheritance + MRO	Multiple inheritance and check MRO

# 7. Multiple Inheritance & MRO
#Q: Demonstrate multiple inheritance and method resolution order.

class A:
    def show(self):
        return "A"
    
class B(A):
    def show(self):
        return "B"
    
class C(A):
    def show(self):
        return "C"
    
class D(B, C):
    pass   # D inherits from B and C

d = D()
print(d.show())  # Output: B (B's show method is called first due to MRO)
# To check the method resolution order (MRO) of class D 
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# The MRO shows the order in which Python looks for methods when they are called on an instance of D.
