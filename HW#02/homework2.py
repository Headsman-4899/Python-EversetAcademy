import math


def arithmetic(a, b, operation):
    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == '/':
        print(a / b)
    else:
        print("Unknown Operation")


def is_year_leap(year):
    print((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)))


def square(a):
    print("perimeter is: ", a * 4)
    print("square is: ", a ** 2)
    print("diagonal is: ", a * math.sqrt(2))


def seasons(month):
    if month == 12 or month == 1 or month == 2:
        print("winter")
    elif month == 3 or month == 4 or month == 5:
        print("spring")
    elif month == 6 or month == 7 or month == 8:
        print("summer")
    elif month == 9 or month == 10 or month == 11:
        print("autumn")
    else:
        print("wrong input")


def is_prime(n):
    if 0 > n > 1000:
        return False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    arithmetic(3, 2, '/')
    is_year_leap(1992)
    square(4)
    seasons(1)
    print(is_prime(11))
