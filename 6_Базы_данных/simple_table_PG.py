from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Определение модели
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Настройка соединения
DATABASE_URL = "postgresql://deusmouse:    @localhost:5432/my_db_1"
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Запрос пользователя с именем "Tor"
user = session.query(User).filter(User.name == 'Tor').first()
print(f'{user=}')
print(f'{user.name=}')
print(f'{user.email=}')
print(f'{user.email is None=}')
