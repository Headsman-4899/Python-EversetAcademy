
users = {"admin": "password", "user": "user_password"}
products = {"apples": 12.99, "oranges": 10.99, "bananas": 7.99}


def admin_page():
    operations = ["add", "update", "delete"]

    def add_product(name, price):
        products[name] = price
        return products

    def update_products(new_product):
        products.update(new_product)
        return products

    def delete_product(name):
        products.pop(name)
        return products

    operation = str(input("Что вы хотите сделать ? (add/update/delete): "))
    if operation in operations:
        if operation == "add":
            print("Введите имя и цену продукта: ")
            name, price = str(input()), float(input())
            print(add_product(name, price))
        elif operation == "update":
            new_products = {}
            count = int(input("Введите кол-во изменяемых продуктов: "))
            print("Введите продукт и цену для обновления: \n")
            for _ in range(count):
                name, price = str(input()), float(input())
                new_products[name] = price
            print(update_products(new_products))
        elif operation == "delete":
            print("Введите имя продукта которое хотите удалить: ")
            name = str(input())
            print(delete_product(name))
        else:
            print("Wrong operation!")

    return products


def user_page():
    cart = []

    def buy_product(name):
        products.pop(name)
        cart.append(name)
        return products

    product_name = str(input("Что вы хотите купить? "))
    if product_name in products:
        print(buy_product(product_name))
        print(cart)

    return cart


def is_authorize(user_name, password):
    if user_name in list(users.keys()):
        if user_name == "admin" and password == "password":
            print(f"Добро пожаловать, {name}")
            admin_page()
            return True
        elif user_name == "user" and password == "user_password":
            print(f"Добро пожаловать, {name}")
            user_page()
            return True
        else:
            print("Данного пользователя не существует!")
            return False
    else:
        return False


if __name__ == '__main__':
    name = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))

    print(is_authorize(name, password))
    # if is_authorize(name, password):
    #     print(f"Добро пожаловать, {name}")
    # else:
    #     print("Данного пользователя не существует!")
