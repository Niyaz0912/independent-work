class PizzaController:
    def __init__(self, pizza):
        self.pizza = pizza

    def update_ingredients(self, new_ingredients):
        self.pizza.change_ingredients(new_ingredients)

    def update_price(self, new_price):
        self.pizza.change_price(new_price)

    def update_weight(self, new_weight):
        self.pizza.change_weight(new_weight)

    def get_pizza_info(self):
        return self.pizza.get_info()