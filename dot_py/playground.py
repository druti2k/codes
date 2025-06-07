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
#Class Inheritince and isintevce() functon
"""Problem:Demonstrate the use of isintance() to check is myTesla is an intance of car and Electriccar."""
#Multiple Inheritance 
"""Problem: create two classes battery and engine, let the electricCar class inherit from both,demeonstrating
# multiple inheritance"""
# class Car:
#     totalcar=0
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.__model=model
#         Car.totalcar+=1

#     def FullName(self):
#         return f"{self.__brand} {self.__model}"
#     def get_brand(self):
#         return self.__brand
#     def fule_type(self):
#         return "desel or petrol"
#     @staticmethod
#     def decription():
#         return "Car is love."
#     @property
#     def model(self):
#         return self.__model
# class Battery:
#     def battery_info(self):
#         return "this is battery"
# class Engine:
#     def engine_info(self):
#         return "this is engine"


# class ElectricCar(Car,Battery,Engine):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size
#     def fule_type(self):
#         return "charge"

# Tesla=ElectricCar("Tesla","Model s","240 Kwh")
# # ElectricCar.battery_size= "340"
# print(Tesla.fule_type())
# Mycar=Car("tata","neon")
# print(Mycar.model)
# print(Tesla.get_brand())
# print(Mycar.FullName())
# print(Car.totalcar)
# print(Car.decription())
# print(isinstance(Tesla,Car))


# print(Tesla.engine_info())

#while true
# while True:
#     num1=int(input("enter a number: "))
#     num2=int(input("enter a number: "))
#     print(num1+ num2)
#     repeat= input("do you want to stop the program:")
#     if repeat=="yes"or "Yes"  "YES":
#         break
    
