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

restaurant = Restaurant("Jollibee", "Fried Chicken")

restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()

