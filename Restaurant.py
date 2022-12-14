class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)
        print("Number Served: " + str(self.number_served))

    def open_restaurant(self):
        print("Restaurant is open!\n")

class User():
    def __init__(self, first_name, middle_initial, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Middle Initial: " + self.middle_initial)
        print("Last Name: " + self.last_name)
        print("Age: " + str(self.age))

    def greet_user(self):
        print("\nHello " + self.first_name + " Welcome!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        self.flavors = flavors

    def display_flavors(self):

ice_cream_stand = IceCreamStand("Vanilla")
ice_cream_stand = IceCreamStand("Strawberry")
ice_cream_stand = IceCreamStand("Chocolate")



