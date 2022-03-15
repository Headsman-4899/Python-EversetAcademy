# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# task 1
def is_digit(n):
    return n.isdigit()


# task 2
def func(num):
    if num <= 1:
        return num
    else:
        return num + func(num - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task1 = is_digit('3')
    print(task1)
    task2 = func(10)
    print(task2)

    # product = lambda x,y: x*y
    # print(product(3, 5))
