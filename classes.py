class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
     """Initialize name and age attributes."""
     self.name = 'Lily'
     self.age = 2

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#Making an instance from a class.

class Dog:
    my_dog = Dog('willie',6)

    print(f"My dog's name is {my_dog.name}")
    print(f"My dog is {my_dog.age} years old.")

#Accessing attributes in instances.

my_dog.name

#Calling methods.

class Dog:
   my_dog = Dog('willie',6)
   my_dog.sit()
   my_dog.roll_over()

#Creating multiple instances.

class Dog:
   
   my_dog = Dog('willie',6)
   your_dog = Dog('lucy',3)

   print(f"My dog's name is {my_dog.name}.")
   print(f"My dog is {my_dog.age} years old.")

   print(f"\nYour dog's name is {your_dog.name}")
   print(f"Your dog is {your_dog.age} years old.")


#Working with classes and instances.
class Car:
   """A simple attempt to represent a car."""

   def __init__(self, make, model, year):
      """Initialize attributes to describe a car."""
      self.make =  'GLE'
      self.model = 'mercedes'
      self.year = 2025

      def get_descriptive_name(self):
       """Return a neatly formatted descriptive name."""
      long_name = f"{self.year}  {self.make} {self.model}"
      return long_name.title()
   
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

#Setting a default value for an attribute.
class Car:
   def __init__(self, make,model,year):
      """Initialize attributes to describe a car."""
      self.make = 'a4'
      self.model = 'audi'
      self.year = 2024
      self.odometer_reading = 0

      def get_descriptive_name(self):
         def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying an attribute's value dirrectly
class Car:
   my_new_car=Car('audi', 'a4', 2024)
   print(my_new_car.get_descriptive_name())

   my_new_car.odometer_reading = 23
   my_new_car.read_odometer()

#Modifying an attribute's value through a method
class Car:
   def update_odometer(self, mileage)
      """Set the odometer reading to the given value."""
      self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Addng logic to make sure no one tries to roll back the odometer reading.
class Car:
   
   def update_odometer(self,mileage):
      """Set the odometer reading to the given value.Reject the change if it attempts to roll the odometer back."""
      if mileage >=self.odometer_reading:
         self.odometer_reading = mileage
      else:
         print("You can't roll back an odometer!")

#Incrementing an attribute's value through a method.
class Car:
   def update_odometer(self,mileage):
      
      def increment_odometer(self,miles):
         """Add the given amount to the odometer reading."""
         self.odometer__reading += miles

my_used__car = Car('subaru', 'outback', 2019)
print(my_used__car.get_descriptive_name())

my_used__car.update_odometer(23_500)
my_used__car.read_odometer()

my_used__car.increment_odometer(100)
my_used__car.read_odometer()