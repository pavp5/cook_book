# Задание № 3

# Список словарей с данными файлов
list_dict = []

# Заполнение списка словарей
with open('1.txt', encoding='utf8') as f:
    rows = f.readlines()
list_dict.append({'name' : '1.txt', 'count' : len(rows), 'rows' : rows})
with open('2.txt', encoding='utf8') as f:
    rows = f.readlines()
list_dict.append({'name' : '2.txt', 'count' : len(rows), 'rows' : rows})
with open('3.txt', encoding='utf8') as f:
    rows = f.readlines()
list_dict.append({'name' : '3.txt', 'count' : len(rows), 'rows' : rows})

# Сортировка списка словарей
sorted_list_dict = sorted(list_dict, key=lambda x: x['count'])

# Запись списка в файл
with open('4.txt', 'w', encoding='utf8') as f:
    for file in sorted_list_dict:
        if isinstance(file, dict):
            f.write(file['name'] + '\n')
            f.write(str(file['count']) + '\n')
            f.writelines(file['rows'])
            f.write('\n')
