class Pizza:
    def __init__(self, name, ingredients, price, weight):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.weight = weight

    def change_ingredients(self, new_ingredients):
        self.ingredients = new_ingredients

    def change_price(self, new_price):
        self.price = new_price

    def change_weight(self, new_weight):
        self.weight = new_weight

    def get_info(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'price': self.price,
            'weight': self.weight
        }