class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        car = Car()
        return car

class BikeFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        bike = Bike()
        return bike

class TruckFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        truck = Truck()
        return truck
