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
    def __init__(self, first_name, middle_initial, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.age = age

    def describe_user(self):
        print("First Name: " + self.first_name)
        print("Middle Initial: " + self.middle_initial)
        print("Last Name: " + self.last_name)
        print("Age: " + str(self.age))

    def greet_user(self):
        print("\nHello " + self.first_name + " Welcome!!!")

restaurant1 = Restaurant("Max", "Main Dish", 20)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("McDonalds", "Fast Food", 19)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Jollibee", "Fast Food", 0)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

user1 = User("Sherlock", "J.", "Holmes", 29)
user1.describe_user()
user1.greet_user()
