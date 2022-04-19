from unittest.mock import Mock
import helper_for_mock


fake_1 = Mock()
print(f'{fake_1=}')
print(f'{fake_1()=}')
print(fake_1(1, 2, 3, test=42))
print(fake_1.called)  # вызывался ли объект вообще
print(fake_1(test=42))
print(fake_1.call_count)  # количество вызовов
print(fake_1.call_args)  # аргументы последнего вызова
fake_1.assert_called_with(test=42)

# можно задать что должен возвращать обьект-пустышка
fake_2 = Mock(return_value=42)
print(fake_2())

# мок-обьект имеет произвольные атрибуты - они тоже мок-обьекты
fake_3 = Mock()
print(fake_3.nonexistent_attr)
fake_3.any_attr = 27
print(fake_3.any_attr)

fake_4 = Mock(return_value=fake_3)
result = fake_4()
print(result.any_attr)

# более подробно про все возможности mock-обьектов можно почитать в доках
# https://docs.python.org/3/library/unittest.mock.html
# и в интернете https://goo.gl/Vcb7y2


# Подведем итоги.

# Недостатки тестов:
#   - им нужно уделять время: писать их.
#   - в процессе развития программы нужно обновлять тесты и писать новые.

# Преимущества тестов:
#   - можно отдавать код на доработку другим программистам, тесты гарантируют что ничего не сломается
#   - можно рефакторить/улучшать код, тесты гарантируют что ничего не сломается
#   - можно портировать ПО на разные платформы, тесты гарантируют что ничего не сломается

# Преимущества в переспективе с лихвой перекрывают недостатки.
# Поэтому писать тесты - просто необходимо!



