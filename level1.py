#!c:\Users\1\AppData\Local\Programs\Python\Python310\python.exe


# Задача 1.1.
# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
print(my_favorite_songs[0:13])
print(my_favorite_songs[-13:])
# второй трек
vtoroy = my_favorite_songs.index(",", my_favorite_songs.index(",")+1)
print(my_favorite_songs[16:vtoroy])
#второй трек с конца
vtor_s_konca = my_favorite_songs.rindex(",", 0, my_favorite_songs.rindex(","))
print(my_favorite_songs[vtor_s_konca+2:-15])

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
#создаем список трех случайных
songs = random.sample(list(my_favorite_songs_dict.keys()), 3)
#общее время этих трех 
total_time = sum([my_favorite_songs_dict[song] for song in songs])
print(f'Три песни звучат {total_time:.2f} минут')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime
d = datetime.timedelta(minutes=total_time)
print(f'Три песни звучат {d.seconds // 60:02d}:{d.seconds % 60:02d}')

# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
mes = int(input("Введите номер месяца: "))
if mes < 1 or mes > 12:
    print("Ошибка: некорректный номер месяца")
elif mes == 2:
    dni = 28
elif mes in (4, 6, 9, 11):
    dni = 30
else:
    dni = 31
print(f"В месяце {mes} - {dni} дней")

# Еще один вариант
m = int(input('Введите номер месяца и нажмите Enter: '))
months = {1:'январь, 31 день', 2:'февраль, 28 дней', 3:'март, 31 день', 4:'апрель, 30 дней', 5:'май, 31 день', 6:'июнь, 30 дней', 7 :'июль, 31 день', 8 : 'август, 31 день', 9 :'сенябрь, 30 дней', 10 :'октябрь, 31 день', 11 :'ноябрь, 30 дней', 12 :'декабрь, 31 день'}

if m in months:
    print(f"Вы ввели {months[m]}")
else:
    print('Такого месяца нет!')
# Задача 1.4.
# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"
for title, cod in titles.items():
    total = 0
    for item in store[cod]:
        total += item['quantity'] * item['price']
    print(f"{title} - {sum([item['quantity'] for item in store[cod]])} шт, стоимость {total} руб")
	
	
