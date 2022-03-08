# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

products = {"apples": 12.99, "oranges": 10.99}


def get_product_price(name):
    print(products[name])


def get_all_products():
    print(products)


def add_product(name, price):
    products[name] = price


def update_products(new_products):
    products.update(new_products)


def delete_product(name):
    products.pop(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    update_products({"apples": 9.99, "bananas": 7.99, "mangoes": 17.99})
    get_all_products()
