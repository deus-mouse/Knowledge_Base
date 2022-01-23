# -*- coding: utf-8 -*-

#
# 16.04 6_Базы_данных
#

# В самом общем смысле база данных (БД) - это набор какой-либо информации.
# расположенную на сервере (на сервере может быть несколько БД),
# состояющую из множества таблиц, которые в свою очередь хранят записи.

# Такая структура напоминает таблицы Excel:
# множество таблиц, состоящих из полей (колонок с заголовками) имеющих строгий тип и строк с данными.




# К базовым типам данных относят:

# -- строки (специальные символы, буквы, цифры, которые в совокупности будут обрабатываться как строки.
#            используются разные типы, зависящие от размера строки и способа выделения памяти для их хранения)
# -- числа (целочисленные: разные типы, в зависимости от охватываемомго диапазона, например от -128 до 127 и тд.
#           дробные: разные типы в зависимости от необходимой точности, например тип хранящий числа
#           с двоичной точностью)
# -- даты (в зависимости от типа даты, используются разные типы её хранения.
#          один тип может хранить только время, другой дату, третий и дату и время или только год)

# Кроме базовых типов, существуют и другие.
# Ими могут быть логические данные, или например графика/звук/видео,
# а некоторые БД позволяют и вовсе создать свой пользовательский тип данных.




# СУБД - система управления базами данных.

# Нередко говоря о БД, люди подразумевают СУБД - набор программного обеспечения,
# которое отвечает за создание и работу с БД.
# Главная функция СУБД - управление данными.
# Она также должна поддерживать языки БД и отвечает за копирование/восстановление данных после сбоев.

# Популярные СУБД:

# SQLite
# - локальная - все части на одной машине
# - open-source

# MySQL
# - серверная - части могут быть расположены на разных машинах
# - open-source

# PostgreSQL
# - серверная
# - open-source

# Oracle
# - серверная
# - закрытые исходники


# Все эти СУБД являются реляционными(sqlite, mysql) и объектно-реляционними (postgresql, oracle) СУБД
# Это говорит о том, что каждый столбец ("field" - поле) имеет определенное уникальное название.
# Такие поля можно объединять и использовать в разных таблицах, создавая специальные связи между ними.


# Для управления такими БД, используется специальный язык программирования SQL (“Structured query language”
# что переводится как "язык структурированных запросов", или же просто "язык запросов")



# Существуют также NoSQL 6_Базы_данных, например MongoDB.
# NoSQL базы не имеют строгой структуры хранения записей и имеют отличный от SQL язык запросов




# Познакомимся с языком запросов поближе с помощью библиотеки sqlite3
# подробная документация - https://docs.python.org/3/library/sqlite3.html
import sqlite3

# Сперва создадим соединение с нашей базой данных.
# В нашем примере БД - файл расположенный на компьютере, он так же может быть расположен и на сервере.
# Важно помнить что в реальных задачах нельзя коммитить базу данных в репозиторий!
conn = sqlite3.connect('external_data/Northwind.sl3')
# Укажем тип получаемых данных
conn.text_factory = bytes
# Создадим курсор - специальный объект, с помощью которого мы сможем делать запросы к БД на языке запросов
cursor = conn.cursor()

# Отбор данных из БД:
# SELECT <список-полей> FROM <имя-таблицы>[ WHERE <условие>]
# Пример:
# Требуется отобрать список заказов,
# для которых значение поля Freight (плата за груз) больше значения 100,
# а регион доставки (ShipRegion) -- 'RJ'
cursor.execute("SELECT * FROM Orders WHERE (Freight > 100) AND (ShipRegion = 'RJ')")

# Получение отобранных значений:
results = cursor.fetchall()
print(f'Здесь выведется список значений, подходящих под заданные условия: {results}')

results_one_more_time = cursor.fetchall()
print(f'А здесь пустой список: {results_one_more_time}')
# Это происходит из-за того, что для повторного получения результата из курсора, необходимо создать новый запрос.

# Попробуем получить именя всех клиентов, фамилии которых начинаются на C:
cursor.execute("SELECT ContactName FROM Customers WHERE ContactName LIKE '% C%'")
another_results = cursor.fetchall()
print(f'Список клиентов: {another_results}')

# Удаление записи
cursor.execute("DELETE FROM Orders WHERE OrderID='10'")
# Изменения необходимо подтвердить:
conn.commit()

# Запись в БД:
cursor.execute("INSERT INTO Orders (OrderID, CustomerID, EmployeeID) VALUES ('10', 'Anton', '5')")
conn.commit()

cursor.execute("SELECT * FROM Orders WHERE OrderID = 10")
changes = cursor.fetchall()
print(f'Внесенные нами изменения: {changes}')

# Закрываем соединение
conn.close()

# Обратите внимание, что мы заполнили только 3 поля, остальные автоматически заполнились значениями None.


# ORM

# Другой подход - ORM (Object Relational Mapping) или Объектно-реляционное отображение
# ORM фреймворк представляет собой промежуточный слой между реляционной СУБД и нашим кодом.
# В итоге запросы к этому слою преобразуются в SQL запросы к БД.
# Кроме того, манипуляции с данными происходят на уровне объектов.
# Классы таких объектов соответствуют таблицам БД,
# а экземпляры этих классов - конкретным записям (строкам) таблиц.

# Преимущества ORM:
# -- Независимость от вида базы данных (код легко изменить под другой вид базы данных)
# -- Развитый интерфейс освобождает от сложной семантики SQL (но не исключает её, при необходимости)
# Недостатки ORM:
# -- Потеря производительности:
#    ORM ускоряет процесс разработки и снижает сложность создания конечного продукта
#    но это приводит к тому, что приложение начинает потреблять больше ресурсов
# -- Частичная потеря специфичной функциональности СУБД

# Наиболее распространенные ORM:
# -- SQLAlchemy - Одна из самых популярных ORM
# -- Django ORM - часть фреймворка Django
# -- Peewee/Pony ORM - небольшие ORM

# Рассмотрим работу с БД на примере Peewee ORM
# подробная документация - http://docs.peewee-orm.com/en/latest/index.html
import peewee
import datetime

# Создадим новую БД, для подключения будем использовать SQLite
database = peewee.SqliteDatabase("external_data/music.db")


class BaseTable(peewee.Model):
    # В подклассе Meta указываем подключение к той или иной базе данных
    class Meta:
        database = database


# Чтобы создать таблицу в нашей БД, нам нужно создать класс
class Artist(BaseTable):
    name = peewee.CharField()  # от типа столбца зависит тип данных, который мы сможем в него записать


class Album(BaseTable):
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()


# Создание таблиц:
database.create_tables([Artist, Album])


# Запись данных в таблицы:
# Один способ с явным save()
new_artist = Artist(name="Newsboys")
new_artist.save()
# Второй способ без явного save()
album_one = Album.create(artist=new_artist,
                         title="Read All About It",
                         release_date=datetime.date(1988, 12, 1),
                         publisher="Refuge",
                         media_type="CD")

# Запись нескольких объектов:
albums = [
    {
        "artist": new_artist,
        "title": "Hell is for Wimps",
        "release_date": datetime.date(1990, 7, 31),
        "publisher": "Sparrow",
        "media_type": "CD"
    },
    {
        "artist": new_artist,
        "title": "Love Liberty Disco",
        "release_date": datetime.date(1999, 11, 16),
        "publisher": "Sparrow",
        "media_type": "CD"
    },
    {
        "artist": new_artist,
        "title": "Thrive",
        "release_date": datetime.date(2002, 3, 26),
        "publisher": "Sparrow",
        "media_type": "CD"
    }
]
# Один из способов:
albums_in_db = Album.insert_many(albums).execute()

# Второй:
bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
for band in bands:
    artist = Artist.create(name=band)
    artist.save()

# Получение одной записи из БД:
# Первый способ:
print(f'Название альбома от издателя "Refuge": {Album.select().where(Album.publisher == "Refuge").get().title}')
# Операция выборки имеет схожие команды с теми, которые мы встречали в языке запросов (select, where)

# Второй способ:
print(f'Название издателя альбома "Read All About It": {Album.get(Album.title == "Read All About It").publisher}')

# Получение нескольких записей из БД:
for album in Album.select():
    print(f'Имя исполнителя: {album.artist.name} Название альбома: {album.title} Дата релиза: {album.release_date}')
