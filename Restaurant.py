class Restaurant():
    
    def __init__(self, restaurant_name, signature_dish_name):
        self.restaurant_name = restaurant_name
        self.signature_dish_name = signature_dish_name
        
    def describe_restaurant(self):
        print("Restaurant Name : " + self.restaurant_name)
        print("Signature Dish : " + self.signature_dish_name)

    def open_restaurant(self):
        print(self.restaurant_name + " is Now Open")
        print("Welcome to " + self.restaurant_name)
        print("We serve the best " + self.signature_dish_name)

class Users():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Hello " + self.first_name + " " + self.last_name)
        print("What's on your order?")

restaurant = Restaurant("Jollibee", "Fried Chicken")

restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()
print("\n")

fname = input(str("What's your first name? "))
lname = input(str("How about your last name? "))
print("\n")

user = Users(fname, lname)

user.describe_user()

