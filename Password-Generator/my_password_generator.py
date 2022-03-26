import random


def generate_password():
    print("Enter a site name and login: ")
    site = str(input('site: '))
    login = str(input('login: '))

    symbols = 'abcdefghijklmnopqrstuvwxyz'
    upper_symbols = symbols.upper()
    chars = list()
    chars.extend(symbols)
    chars.extend(upper_symbols)
    chars.extend('-()[]!@#$')
    chars.extend('0123456789')

    generated_password = ''
    random_length = random.randint(8, 15)
    for i in range(random_length):
        generated_password += random.choice(chars)

    result = site + ' - ' + login + ' - ' + generated_password

    try:
        with open("password.txt", "a") as output:
            output.write(result + '\n')
            output.close()
    except IOError:
        print("save password error!")

    print(result)


# def save_password():
#
#
# def update_password():
#     with open("password.txt", "w") as output:
#         output.write(generate_password())


def delete_passwords():
    try:
        with open("password.txt", "w+") as output:
            output.write("")
            output.close()
            print("passwords are deleted successfully!")
    except IOError:
        print("delete password error!")


generate_password()
# save_password()
# update_password()
# delete_passwords()