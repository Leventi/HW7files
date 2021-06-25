import os
import operator
from pathlib import Path
from pprint import pprint

cook_book = {}

path = Path.cwd() / 'files' / 'cook_book' / 'recipes.txt'
with open(path, 'r', encoding="utf-8") as file:
    for line in file:                                   #Идём по строкам
        title = line.strip()                            #Первая строка
        count = file.readline().strip()                 #Вторая строка

        list_of_ingredient = []
        for i in range(int(count)):                     #Начинаем обход уже с третьей строки
            ingredient = file.readline().strip()        #Третья строка
            ingredient_list = ingredient.split('|')     #Разбиваем на список по разделителю
            ingredients = {'ingredient_name': ingredient_list[0],
                           'quantity': int(ingredient_list[1]),
                           'measure': ingredient_list[2]
                           }                            #Формируем словарь с ингридиентами
            # print(ingredients)

            list_of_ingredient += [ingredients]         #Записываем словари в список
            # print(dish_list)
        cook_book[title] = list_of_ingredient           #Собираем словарь {Блюдо : [список с ингредиентами]}
        file.readline().strip()                         # Проходим пустую строку

    # Готовый словарь
    # pprint(cook_book)


#Расчёт количества ингредиентов для N персон
dish_list = ['Омлет', 'Фахитос', 'Картоха жареная']
persons = 3

def get_shop_list_by_dishes(dish_list, persons):
    shop_list = {}

    for dish in dish_list:
        for ing in cook_book[dish]:
            ing['quantity'] = ing['quantity']*persons

            if ing['ingredient_name'] not in shop_list:
                shop_list[ing['ingredient_name']] = {
                    'quantity': ing['quantity'],
                    'measure': ing['measure']
                }

            else:
                ing['quantity'] += shop_list[ing['ingredient_name']]['quantity']
                shop_list[ing['ingredient_name']]['quantity'] += shop_list[ing['ingredient_name']]['quantity']

                shop_list[ing['ingredient_name']] = {
                    'quantity': ing['quantity'],
                    'measure': ing['measure']
                }

    return pprint(shop_list)

#Вывод результата функции расчёта количества ингредиентов - Раскомментировать
# get_shop_list_by_dishes(dish_list, persons)



#Чтение списка файлов
path = os.path.join(os.getcwd(), 'files\sort_files')
# print(path)


def FileSort(path):
    file_dict = {}

    #Собираем словарь {название файла: количество строк}
    #Идем по всем поддиректориям и собираем вообще все файлы
    for dirpath, dirnames, files in os.walk(path):
        for filename in files:
            #Фильтруем по расширению
            if filename.endswith('.txt'):
                #Считаем количество строк и формируем словарь
                with open(f'{dirpath}/{filename}') as f:
                    line_count = 0
                    for line in f:
                        line_count += 1

                        file_dict[filename] = line_count, dirpath

    #Сортируем словарь
    sorted_tuples = sorted(file_dict.items(), key=operator.itemgetter(1))
    sorted_file_dict = {k: v for k, v in sorted_tuples}

    for i, n in sorted_file_dict.items():
        # print(i)
        # print(n[1])
        # print(list(sorted_file_dict.values())[n][1])
        with open(f'{n[1]}/{i}', 'r', encoding='utf-8') as file_:
            print(f'\nНаименование файла: {i}\nКоличество строк: {n[0]}\nСодержимое:\n{file_.read()}')

# FileSort(path)

