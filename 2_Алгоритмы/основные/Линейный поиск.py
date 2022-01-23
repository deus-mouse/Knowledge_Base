# Линейный поиск
# Страдает скорость
 

names = ['Роман', 'Лена', 'Денис', 'Тоня']
search_for = 'Тоня'
def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # вохвращаем индекс

    return None  # или None если не найдено

print(linear_search(names, search_for))

