from web_pizza_project.Pasta.pasta_product import MenuPasta


class ChangePasta:
    def __init__(self, position):
        if position in MenuPasta.menu:
            self.position = {position: MenuPasta.menu[position]}
        else:
            self.position = {position: [0, 0, []]}

    def set_new_cost_price(self, position, price):
        self.position[position][0] = price
        return self.position

    def set_new_sale_price(self, position, price):
        if price < self.position[position][0]:
            return "Невозможно установить цену ниже себестоимости"
        else:
            self.position[position][1] = price
            return self.position

    def set_ingredients(self, position, *args):
        self.position[position][2] = list(args)
        return self.position

    def add_to_menu(self, position):
        MenuPasta.menu[position] = self.position[position]
        return MenuPasta.menu

    @staticmethod
    def remove_from_menu(position):
        if position in MenuPasta.menu:
            removed_position = MenuPasta.menu.pop(position)
            return removed_position, MenuPasta.menu
        else:
            return "Позиции нет в меню"
