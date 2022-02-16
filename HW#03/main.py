# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_symbol(ch):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(1, 6):
        print(ch * i)


def sum_of_numbers():
    sum = 0
    n = int(input('>>>'))
    if n < 0:
        print("input cannot be less than 0! Please, try again.")
    while n != 0:
        sum += n % 10
        n //= 10
    print(sum)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_symbol('*')
    sum_of_numbers()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
