# Определение модели Pizza
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


# Определение контроллера PizzaController
class PizzaController:
    def __init__(self, your_pizza):
        self.pizza = your_pizza

    def update_ingredients(self, new_ingredients):
        self.pizza.change_ingredients(new_ingredients)

    def update_price(self, new_price):
        self.pizza.change_price(new_price)

    def update_weight(self, new_weight):
        self.pizza.change_weight(new_weight)

    def get_pizza_info(self):
        return self.pizza.get_info()


# Определение представлений
class FullInfoView:
    def display(self, pizza_info):
        print(f"Название: {pizza_info['name']}")
        print(f"Состав: {pizza_info['ingredients']}")
        print(f"Цена: {pizza_info['price']} руб.")
        print(f"Вес: {pizza_info['weight']} г.")


class IngredientsAndWeightView:
    def display(self, pizza_info):
        print(f"Состав: {pizza_info['ingredients']}")
        print(f"Вес: {pizza_info['weight']} г.")


class PriceView:
    def display(self, pizza_info):
        print(f"Цена: {pizza_info['price']} руб.")


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр модели
    pizza = Pizza("Маргарита", "Томатный соус, моцарелла, базилик", 500, 400)

    # Создаем контроллер для управления моделью
    controller = PizzaController(pizza)

    # Создаем представления
    full_info_view = FullInfoView()
    ingredients_and_weight_view = IngredientsAndWeightView()
    price_view = PriceView()

    # Отображаем всю информацию о пицце
    full_info_view.display(controller.get_pizza_info())

    # Отображаем состав и вес
    ingredients_and_weight_view.display(controller.get_pizza_info())

    # Отображаем только цену
    price_view.display(controller.get_pizza_info())

    # Изменяем состав и цену
    controller.update_ingredients("Томатный соус, моцарелла, базилик, оливки")
    controller.update_price(600)

    # Снова отображаем всю информацию о пицце
    full_info_view.display(controller.get_pizza_info())
