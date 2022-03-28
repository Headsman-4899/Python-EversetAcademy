import random
from ChromePasswordsStealer import ChromePasswordsStealer

result = {
    'kaspi': ['user', 'kaspi-password'],

}


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

    new_dict = {site: [login, generated_password]}
    result.update(new_dict)

    try:
        with open("password.txt", "w") as output:
            output.write(str(result) + '\n')
            output.close()
    except IOError:
        print("Save password error!")

    print(result)


# def save_password():
#     stealer = ChromePasswordsStealer("passwords", True)
#     stealer.get_database_cursor()
#     stealer.get_key()
#     for url, username, password in stealer.get_credentials():
#         if url == 'https://wsp.kbtu.kz/':
#             try:
#                 with open("password.txt", "a") as output:
#                     output.write(url + " - " + username + " - " + password + '\n')
#             except IOError:
#                 print("Save password error!")
#     stealer.save_and_clean()


def update_password(site, login, password):
    new_result = {site: [login, password]}
    result.update(new_result)

    try:
        with open("password.txt", "w") as output:
            output.writelines(str(result) + '\n')
    except IOError:
        print('Update password error!')


def delete_password(site):
    result.pop(site)
    try:
        with open("password.txt", "w+") as output:
            output.write(str(result))
            output.close()
            print("passwords are deleted successfully!")
    except IOError:
        print("Delete password error!")


generate_password()
# save_password()
# update_password('qaz', 'user', 'ewqeqw')
# delete_passwords()