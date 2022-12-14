class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """Model a battery for electric car."""

    def __init__(self, battery_size = 70):
        """Battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Prin the range of this battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    

class ElectricCar(Car):
    """Aspects of car for electric cars"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    

    def fill_gas_tank():
        """Electric cars run by electric"""
        print("This car runs by electric and doesn't need a gas tank")

    
my_tesla = ElectricCar('tesla', 'model s', 2006)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
