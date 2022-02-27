# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # task 1
    print("task 1")
    l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = [i for i in l if i < 5]
    print(result)
    print('\n')

    # task 2
    print("task 2")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = [i for i in a for j in b if i == j]
    print(result)
    print('\n')

    # task 3
    print("task 3")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a[0], a[len(a)-1])
    print('\n')

    # task 4
    print("task 4")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = [i for i in a if i not in b]
    print(result)

