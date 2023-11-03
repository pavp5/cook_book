# Задание 1

# Возвращает словарь кулинарной книги
def get_cook_dict(file_path, encoding):
    cook_book = {} 
    dish_name = ''  
    dish_ingredients = []
    with open(file_path, encoding=encoding) as file:
        for line in file:
            line = line.strip().split(' | ')
            # название блюда или количество ингредиентов
            if len(line) < 3:           
                # считаем, что длина названия блюда больше 2-x символов
                if len(line[0]) > 2:
                    dish_name = line[0]
                    dish_ingredients = []
            # ингредиенты
            else:
                if dish_name != '':
                    dish_ingredients.append({'ingredient_name' : line[0], 'quantity' : int(line[1]), 'measure' : line[2]})
                    cook_book[dish_name] = dish_ingredients                    
    return cook_book

# print(get_cook_dict('recipes.txt', 'utf8'))


# Задание 2

# Возвращает словарь с перечнем продуктов и их количеством на указанный перечень блюд и количество персон 
def get_shop_list_by_dishes(dish_list, person_count):
    shop_dict = {}
    if isinstance(dish_list, list) and isinstance(person_count, int):       
        cook_book = get_cook_dict('recipes.txt', 'utf8')
        # цикл по списку блюд
        for dish_name in dish_list:
            if dish_name in cook_book.keys():
                # текущее блюдо
                dish = list(cook_book.get(dish_name))
                # цикл по ингредиентам текущего блюда
                for dish_ingredient in dish:
                    dish_ingredient = dict(dish_ingredient)
                    if not dish_ingredient['ingredient_name'] in shop_dict.keys():
                        shop_dict[dish_ingredient['ingredient_name']] = {
                            'measure' : dish_ingredient['measure'], 
                            'quantity' : int(dish_ingredient['quantity']) * person_count}
                    else:
                        shop_dict[dish_ingredient['ingredient_name']] = {
                            'measure' : dish_ingredient['measure'], 
                            'quantity' : int(dish_ingredient['quantity']) * person_count +
                            int(dict(shop_dict[dish_ingredient['ingredient_name']])['quantity'])}

    return shop_dict

# print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))




    




