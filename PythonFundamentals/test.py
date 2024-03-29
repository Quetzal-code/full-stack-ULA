num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)

# Excersice 2
def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()