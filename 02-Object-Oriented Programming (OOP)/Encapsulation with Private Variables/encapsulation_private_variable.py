# #	Polymorphism	Method overriding using base and derived class
# 5. Encapsulation with Private Variables
# Q: Create a class with a private variable and access it using getter/setter methods.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
    def get_balance(self):
        return self.__balance  # Getter method

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount  # Setter method
        else:
            print("Balance cannot be negative.")

acc = BankAccount(1000)
acc.deposit(500)
print("Current Balance:", acc.get_balance())  # Accessing private variable using getter method
