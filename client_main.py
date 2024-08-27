from Pizza.pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza
from Pasta.pasta_creator import PastaCreator, CreateMenuPasta, CreateOwnPasta


def client_code(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


def pasta_client_code(creator: PastaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pasta(order))
    print(creator.cook_pasta(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    menu_pizza = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
    menu_pasta = ["Спагетти", "Фетучини Альфредо", "Карбонара", "Пенне Болоньезе", "Тортильони с мясом"]

    print("Добро пожаловать в наше заведение!")
    print("Что вы хотите заказать? (введите 'пицца' или 'паста')")
    order_type = input(">>> ").lower()

    if order_type == "пицца":
        print("Выберите пиццу из меню:")
        for pizza in menu_pizza:
            print(pizza)
        user_order = input("Введите ваш заказ: ")
        if user_order in menu_pizza:
            client_code(CreateMenuPizza(), user_order)
        else:
            client_code(CreateOwnPizza(), user_order)
    elif order_type == "паста":
        print("Выберите пасту из меню:")
        for pasta in menu_pasta:
            print(pasta)
        user_order = input("Введите ваш заказ: ")
        if user_order in menu_pasta:
            pasta_client_code(CreateMenuPasta(), user_order)
        else:
            pasta_client_code(CreateOwnPasta(), user_order)
    else:
        print("Извините, мы не поняли ваш заказ. Пожалуйста, попробуйте еще раз.")
