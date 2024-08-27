from abc import ABC, abstractmethod
from web_pizza_project.Pasta.pasta_product import MenuPasta, OwnPasta
import json
import time


class PastaCreator(ABC):
    @abstractmethod
    def make_pasta(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def cook_pasta(self, order):
        pass

    @abstractmethod
    def save_order_to_json(self, order):
        pass


class CreateMenuPasta(PastaCreator):
    def __init__(self):
        self.menu_pasta = MenuPasta()

    def make_pasta(self, order):
        return self.menu_pasta.make_pasta(order)

    def add_additional_ingredient(self):
        return self.menu_pasta.add_additional_ingredient()

    def cook_pasta(self, order):
        return self.menu_pasta.cook_pasta(order)

    def save_order_to_json(self, order):
        menu_pasta = {order: self.menu_pasta.menu[order]}
        menu_pasta[order][2].extend(self.menu_pasta.additional_ingredients)
        if menu_pasta:
            with open(f"Pasta/orders/{round(time.time(), 2)}_{order}.json", 'w', encoding='utf-8') as fp:
                json.dump(menu_pasta, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"


class CreateOwnPasta(PastaCreator):
    def __init__(self):
        self.own_pasta = OwnPasta()

    def make_pasta(self, order):
        return self.own_pasta.make_pasta(order)

    def add_additional_ingredient(self):
        return self.own_pasta.add_additional_ingredient()

    def cook_pasta(self, order):
        return self.own_pasta.cook_pasta(order)[0]

    def save_order_to_json(self, order):
        own_pasta_data = self.own_pasta.cook_pasta(order)[1]
        if own_pasta_data:
            with open(f"Pasta/orders/{round(time.time(), 2)}_{order}.json", "w", encoding='utf-8') as fp:
                json.dump(own_pasta_data, fp, ensure_ascii=False, indent=2)
        return "Заказ сохранен в файл orders.json"
