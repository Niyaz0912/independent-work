class ChangePizza:
    def __init__(self, position, menu):
        if position in menu:
            self.position = {position: menu[position]}
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

    def add_to_menu(self, position, menu):
        menu[position] = self.position[position]
        return menu

    @staticmethod
    def remove_from_menu(position, menu):
        if position in menu:
            removed_position = menu.pop(position)
            return removed_position, menu
        else:
            return "Позиции нет в меню"


class ChangePasta:
    def __init__(self, position, menu):
        if position in menu:
            self.position = {position: menu[position]}
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

    def add_to_menu(self, position, menu):
        menu[position] = self.position[position]
        return menu

    @staticmethod
    def remove_from_menu(position, menu):
        if position in menu:
            removed_position = menu.pop(position)
            return removed_position, menu
        else:
            return "Позиции нет в меню"


class Menu:
    menu_pizza = {
        "Гавайская": [100, 150, ["сырный соус", "ветчина", "филе цыпленка", "ананасы", "сыр моцарелла", "базилик"]],
        "Грибная": [80, 120, ["чесночный соус", "ветчина", "свежие шампиньоны", "сыр моцарелла", "базилик"]],
        "Сырный цыпленок": [110, 155, ["сырный соус", "филе цыпленка", "свежие томаты", "сыр моцарелла", "базилик"]],
        "Пепперони": [120, 170, ["пицца-соус", "пепперони", "сыр моцарелла", "базилик"]],
        "Тунец - тысяча островов": [200, 300,
                                    ["соус тысяча островов", "тунец", "маслины", "сыр моцарелла", "лимон", "базилик"]],
    }
    menu_pasta = {
        "Спагетти": [100, 150, ["спагетти", "томатный соус", "чеснок", "оливковое масло"]],
        "Фетучини Альфредо": [120, 170, ["фетучини", "сливочный соус", "пармезан", "петрушка", "перец"]],
        "Карбонара": [130, 180, ["паста", "яйцо", "бекон", "пармезан", "перец"]],
        "Пенне Болоньезе": [110, 160, ["пенне", "белое вино", "мясной фарш", "томатный соус"]],
        "Тортильони с мясом": [150, 210, ["тортильони", "мясо", "чили", "помидоры", "оливковое масло"]],
    }


# Create instance of the Menu containing pizza and pasta
menu = Menu()
menu_pizza = menu.menu_pizza
menu_pasta = menu.menu_pasta

# Create instances of ChangePizza and ChangePasta
pizza_changer = ChangePizza('Грибная', menu_pizza)
pasta_changer = ChangePasta('Спагетти', menu_pasta)

# Testing for Pizza
print("--- Pizza Management ---")
print(pizza_changer.set_new_cost_price('Грибная', 200))
print(pizza_changer.set_new_sale_price('Грибная', 300))
print(pizza_changer.set_ingredients('Грибная', "чесночный соус", "колбаса", "шампиньоны", "сыр моцарелла", "базилик"))
print(pizza_changer.add_to_menu('Грибная', menu_pizza))
removed_data, new_menu_pizza = ChangePizza.remove_from_menu('Грибная', menu_pizza)
print(removed_data)
print(new_menu_pizza)
print(ChangePizza.remove_from_menu('Грибная', menu_pizza))

# Testing for Pasta
print("--- Pasta Management ---")
print(pasta_changer.set_new_cost_price('Спагетти', 250))
print(pasta_changer.set_new_sale_price('Спагетти', 350))
print(pasta_changer.set_ingredients('Спагетти', "томатный соус", "оливковое масло", "базилик"))
print(pasta_changer.add_to_menu('Спагетти', menu_pasta))
removed_data, new_menu_pasta = ChangePasta.remove_from_menu('Спагетти', menu_pasta)
print(removed_data)
print(new_menu_pasta)
print(ChangePasta.remove_from_menu('Спагетти', menu_pasta))
