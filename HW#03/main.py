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
        n = int(input('>>>'))

    while n != 0:
        sum += n % 10
        n //= 10
    print(sum)


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            print(index)
            break
        index += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_symbol('*')
    # sum_of_numbers()
    fruit = 'banana'

    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        print(letter + suffix)

    s = 'Python'
    for i in range(len(s)):
        print(s[i])


    s = 'London isthe Capital of GB.'
    new_s_1 = s[0:9]
    new_s_2 = s[9:]
    print(new_s_1 + " " + new_s_2)

    find('qwerty', 'w')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
