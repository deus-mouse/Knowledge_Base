# ORM

# Другой подход - ORM (Object Relational Mapping) или Объектно-реляционное отображение
# ORM фреймворк представляет собой промежуточный слой между реляционной СУБД и нашим кодом.
# В итоге запросы к этому слою преобразуются в SQL запросы к БД.
# Кроме того, манипуляции с данными происходят на уровне объектов.

# Классы таких объектов соответствуют таблицам БД,
# а экземпляры этих классов - конкретным записям (строкам) таблиц.

# Типы данных:
# Строки
# Числа
# Даты

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
