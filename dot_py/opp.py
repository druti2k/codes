# basic class and objects:
"""problem:create a car class with attributes(variabels) like brand and model.
then create an instance of this class."""
# class method and self
"""problem: Add a methods to the car class to disply the full name of the car(brand and model)."""
#  Inheritance
""" Problem: Create an electric car class that inherit from car class and has an additional attribute"""
# Encapsulaton
"""Problem: modify the car class to encapsulate the brand attribute, making it private, and provide a gatter method for it."""
# Polymorphism
"""Problem: Demonstrate polymorphism by drfining a method fule_type in both car and electric car classes, but with different behaviors."""
# Class variable
"""Problem: Add a class Variable to car that keeps track of the number of car created"""
#Stactic method
"""Problem: Add a static method to the car class that retuurn a general decription of a car.."""
#Property Decorator
"""Problem: use a property decorator in car class to make the model atttribute read only."""
#Clasa Inheritince and isintevce() functon
"""Problem:Demonstrate the use of isintance() to check is myTesla is an intance of car and Electriccar."""
#Multiple Inheritance 
"""Problem: create two classes battery and engine, let the electricCar class inherit from both,demeonstrating
multiple inheritance"""


class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand= brand #(using "__" we change the attribute private)
        self.__model=model
        Car.total_car+=1
    def fullName(self):
        return f"{self.__brand} {self.__model}"  # f"{} {}" formated string
    def get_brand(self): #{for providing gatter method we have to use get_ syntex}
        return self.__brand + " Car"
    def fule_type(self):
        return "petrol or diesel"
    @staticmethod  #{it called decorators}
    def Description():
        return "Car is love"
    @property
    def model(self):
        return self.__model

class Battery:
    def battery_info(self):
        return "This is battery"
class Engine:
    def engine_info(self):
        return "This is V12"
class ElectricCar(Car,Battery,Engine):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fule_type(self):
        return "charge"

Tesla=ElectricCar("tesla","Model s","89kwh")
print(Tesla.battery_info())

# print(Car.Description())
# print(myTesla.fullName())   
# print(myTesla.battery_size)      
# print(myTesla.get_brand())      
# Car("Tata","Neon")
# print(pcar.fule_type())
# print(myTesla.fule_type())


# instance
# myCar=Car("tata","nexon")
# myCar.model="xor"
# print(myCar.brand)
# print(myCar.model)
# print(myCar.model)
# print(myCar.fullName())