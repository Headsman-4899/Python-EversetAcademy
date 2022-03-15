# воссоздайте функционал CRM системы управления онлайн магазина по продаже различных товаров


# Авторизация
users = {'admin': 'password', 'zhalgas': 'qwertyzx12'}
'''
Вам дан словарь users
добавьте в него пользователя admin с паролем password
добавьте в него пользователя себя с вашим паролем
'''
'''
Напишите функцию authorize() которая спрашивает логин и пароль у пользователя
и сравнивает с теми что храняться в словаре users
в случае совпадения функция выдает сообщение "Добро пожаловать, имя_пользователя"
а в ином случае выдает мообщение такого пользователя не существует 
'''


def authorize():
    login = input("Enter your name: ")
    if login == 'exit':
        return
    if login == 'admin':
        password = input("Enter your password: ")
        if password == 'password':
            admin_page()
    if login in users:
        password = input("Enter your password: ")
        if users[login] == password:
            print("Welcome, ", login)
            user_page()
        else:
            print("Incorrect password")
            authorize()
    else:
        print("Login is not in the system")
        authorize()


# Вход
'''
Если вы вашли как админ то запускается функция admin_page()
Если вы вашли как обычный пользователь то запускается функция user_page()

p.s для хранения информаций об товаре используйте удобный для вас тип для хранения данных
list, tuple или dict и заполните их данными минимум 5шт
'''

products = [{'apple': 45}, {'meat': 120}, {'tomato': 35}, {'carrot': 23}, {'potato': 25}]


def admin_page():
    print("welcome to admin page")
    choice = input(
        "Select what kind of operation you want to do? \n print: \n add \n update \n delete \n show \n exit \n =>")
    if choice == 'add':
        add_product()
    if choice == 'update':
        update_product()
    if choice == 'delete':
        delete_product()
    if choice == 'show':
        show_product()


def show_product():
    print(products)
    # admin_page()


def add_product():
    p_name = input("Product name: ")
    p_price = int(input("Product price: "))
    products.append({p_name: p_price})
    admin_page()


def update_product():
    p_name = input("Product name: ")
    for product in products:
        if p_name in product:
            p_price = int(input("Product price: "))
            product[p_name] = p_price
    admin_page()


def delete_product():
    p_name = input("Product name: ")
    for product in products:
        if p_name in product:
            products.remove(product)
    admin_page()


def exitt():
    print("Goodbye!")
    authorize()


def user_page():
    products = [{'apple': 45}, {'meat': 120}, {'tomato': 35}, {'carrot': 23}, {'potato': 25}]
    buy_product()


def buy_product():
    show_product()
    choice = input("select which product you want to buy from above list(or exit): ")
    if choice == 'exit':
        exitt()
    for product in products:
        if choice in product:
            print(choice, ' is added to cart', 'price is', product[choice])
            user_page()


'''
В admin_page нужно реализовать функционал добавления, удаления и изменения товаров
то есть цены, описания итп

'''
'''
В user_page нужно реализовать функционал покупки товаров
'''

'''
Внутри admin_page() создайте функцию
add_product() - добавление нового
updte_product()- изменения товара
delete_product() - удаление товара
'''

'''
Внутри user_page() создайте функцию
buy_product() - покупка
'''