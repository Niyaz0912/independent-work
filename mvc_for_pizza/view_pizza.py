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
