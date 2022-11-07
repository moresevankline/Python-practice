class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Restaurant Name : " + self.restaurant_name)
        print("Cuisine Type : " + self.cuisine_type)

    def open_restaurant(self):
        print("Welcome the restaurant is open!!!")

restaurant = Restaurant("Jollibee", "Fastfood")

restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()

