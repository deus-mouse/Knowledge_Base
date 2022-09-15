"""
Занятие 1. Скорая помощь
Бригада скорой помощи выехала по вызову в один из отделенных
районов. К сожалению, когда диспетчер получил вызов, он успел записать
только адрес дома и номер квартиры К1, а затем связь прервалась.
Однако он вспомнил, что по этому же адресу дома некоторое время назад
скорая помощь выезжала в квартиру Ка, которая расположена в подъезда
Ра на этаже N2. Известно, что в доме М этажей и количество квартир на
каждой лестничной площадке одинаково. Напишите программу, которая
вычисляет номер подъезда Р1 и номер этажа N1 квартиры К,.

k - квартира
p - подъезд
n - этаж
M - этажей в подъезде

"""


def count_appartments_on_floor(k, n, p, M):
    total_floors = (p - 1) * M + n
    res = k // total_floors
    print(f'count_appartments_on_floor = {res}')
    return res


def foo(k_1, k_2, n_2, p_2, M):
    total_floors = k_1 // count_appartments_on_floor(k_2, n_2, p_2, M)
    print(f'total_floors = {total_floors}')


    p_1 = (total_floors // M) if (total_floors % M == 0) else (total_floors // M + 1)
    n_1 = total_floors % M if total_floors > M else total_floors
    return p_1, n_1


print(f'{foo(16, 43, 2, 3, 4)=}')
