from abc import ABC, abstractmethod


class PastaProduct(ABC):

    @abstractmethod
    def make_pasta(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def cook_pasta(self, order):
        pass


class MenuPasta(PastaProduct):
    menu = {
        "Спагетти": [100, 150, ["спагетти", "томатный соус", "чеснок", "оливковое масло"]],
        "Фетучини Альфредо": [120, 170, ["фетучини", "сливочный соус", "пармезан", "петрушка", "перец"]],
        "Карбонара": [130, 180, ["паста", "яйцо", "бекон", "пармезан", "перец"]],
        "Пенне Болоньезе": [110, 160, ["пенне", "белое вино", "мясной фарш", "томатный соус"]],
        "Тортильони с мясом": [150, 210, ["тортильони", "мясо", "чили", "помидоры", "оливковое масло"]],
    }
    additional_ingredients = []

    def make_pasta(self, order):
        if order in self.menu.keys() and self.additional_ingredients:
            return f"Формируем пасту {order} с составом:\n{', '.join(self.menu[order][2])}\nДополнительно: {', '.join(self.additional_ingredients)}"
        elif order in self.menu.keys():
            return f"Формируем пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"

    def add_additional_ingredient(self):
        ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.additional_ingredients.append(ingredient)
            ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")

    def cook_pasta(self, order):
        if not self.additional_ingredients:
            return f"Варим пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"
        else:
            return f"Варим пасту {order} с дополнительными ингредиентами:\n{', '.join(self.additional_ingredients)}\n"


class OwnPasta(PastaProduct):
    ingredients = []

    def make_pasta(self, order):
        ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.ingredients.append(ingredient)
            ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        print()
        return f"Формируем пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}"

    def add_additional_ingredient(self):
        pass

    def cook_pasta(self, order):
        own_pasta = {order: [150, 200, self.ingredients]}
        return f"Варим пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}\n", own_pasta
