#When we create a child class, the parent class must be part of the current file and must appear before the child class in the file.
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = 'G4'
        self.model = 'subaru'
        self.year = 2025
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer  reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer__reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer__reading +=miles

class ElectricCar(Car):#The name of the parent class must be included in brackets.
    """Represent aspects of a car, specific to the electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)#super () is a special function that allows you to call a method from the parent class.

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

#Defining attributes and methods for the child class.
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = 'G4'
        self.model = 'subaru'
        self.year = 2025
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer  reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer__reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer__reading +=miles

class ElectricCar(Car):#The name of the parent class must be included in brackets.
    """Represent aspects of a car, specific to the electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)#super () is a special function that allows you to call a method from the parent class.
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())   
my_leaf.describe_battery() 

#Overriding methods from the parent class.This ca be done by defining a mathod in the child class with the same name as the method you want to override in the parent class.

#Instances as attributes.
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = 'G4'
        self.model = 'subaru'
        self.year = 2025
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer  reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer__reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer__reading +=miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size =40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size ==40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):#The name of the parent class must be included in brackets.
    """Represent aspects of a car, specific to the electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)#super () is a special function that allows you to call a method from the parent class.
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())   
my_leaf.battery.describe_battery() 
my_leaf.battery.get_range()
