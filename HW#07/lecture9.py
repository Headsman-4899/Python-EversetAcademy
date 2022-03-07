
import random

f = open('names.txt','r')

names = []
for i in range(500):
    name = f.readline()
    names.append(name)

f.close()


res = []
for name in names:
    res.append(name.strip())

numbers = []
for i in range(500):
    number = random.randint(1000, 10001)
    numbers.append(number)


address_book = {}

for i in range(500):
    address_book[res[i]] = numbers[i]

nms = []
for i in range(500):
    nms.append([res[i], numbers[i]])


def search_ab(name):
    return name, number


spisok = ['Zhalgas', 'Beksultan', 'Oraz', 'Aigerim', 'Zhalgas', 'Zhalgaskhan']

def check_duplicate():
    d = {}
    for element in spisok:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d
