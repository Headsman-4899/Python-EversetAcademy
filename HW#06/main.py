# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def printall(*args):
    print(args)


def task_6():
    t = ()
    for idx in range(5):
        var = int(input("Введите любое число:"))
        t += (var,)

    sum = 0
    for i in t:
        sum += i

    average = sum / len(t)
    print("Самое большое число:", max(t))
    print("Наименьшее число:", min(t))
    print("Сумма всех чисел:", sum)
    print("Среднее значение:", average)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # task 1
    a = 5
    b = 10
    a, b = b, a
    print(a, b)


    # task 2
    t = (1, -20, 68, 10, 54)
    maxi = t[0]
    for n in t:
        if maxi < n+1:
            maxi = n
    print(maxi)
    print(max(t))


    # task 3
    t = (1, 12, 33, 8, 1)
    odd, even = 0, 0

    for i in t:
        if i % 2 == 0:
            even += i
        else:
            odd += i

    print("Сумма четных чисел равна", even)
    print("Сумма нечетных числе равна", odd)


    # task 4
    T1 = ("Yernar", "Aziza", "Zhako", "Nur")
    result = []
    for i in T1:
        result.append(len(i))
    print(result)


    # task 5
    T1 = (("Andrey", 75), ("Vasya", 35), ("Naruto", 50), ("Sasuke", 60))
    total = 0
    for name, point in T1:
        total += point

    print(total//len(T1))

    # task 6
    task_6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
