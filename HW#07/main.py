# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

products = {"apples": 12.99, "oranges": 10.99}


def get_product(name):
    print(products[name])


def get_all_products():
    print(products)


def add_product(name, price):
    products[name] = price


def update_product(name, price):
    products.update({name: price})


def delete_product(name):
    products.pop(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(products)
    delete_product("oranges")
    get_all_products()