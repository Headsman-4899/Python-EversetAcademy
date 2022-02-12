# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def my_info():
    name = "Daulet"
    surname = "Kareneyev"
    age = 20
    print("Hi, my name is", name, surname, ", I am", age, "years old.\n")


def first_func(n):
    tax = n * 0.19
    print(n - tax)


def second_func(n):
    price = 2500
    discount = 0.8
    first_delivery = 300
    next_delivery = 450
    book_price_with_discount = price * discount

    total_for_first_delivery = book_price_with_discount + first_delivery
    total_for_next_delivery = book_price_with_discount + next_delivery

    i = 2
    total = total_for_first_delivery
    while i <= n:
        total += total_for_next_delivery
        i += 1

    print(total)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_info()

    width = 17  # ширина
    height = 12.0  # высота
    delimiter = '.'

    print(width / 2, type(width / 2))
    print(width / 2.0, type(width / 2.0))
    print(height / 3, type(height / 3))
    print(1 + (2 * 5), type(1 + (2 * 5)))
    print(delimiter * 5, type(delimiter * 5))

    first_func(335000)
    second_func(12)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
