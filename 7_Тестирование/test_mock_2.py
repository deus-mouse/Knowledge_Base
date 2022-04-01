import unittest
from unittest.mock import Mock
import helper_for_mock


_test_data = """
1234567
12345
123456789
12
"""


class FakeResult:

    def __init__(self):
        self.text = _test_data

# 3
class ExternalResourceGetterTest3(unittest.TestCase):

    def test_normal(self):
        getter = helper_for_mock.ExternalResourceGetter(url='bla-bla-bla')
        fake_get_result = Mock(return_value=FakeResult())
        helper_for_mock.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


# 4 без FakeResult самодостаточный класс
class ExternalResourceGetterTest4(unittest.TestCase):

    def test_normal(self):
        getter = helper_for_mock.ExternalResourceGetter(url='bla-bla-bla')
        fake_result = Mock()
        fake_result.text = _test_data
        fake_get_result = Mock(return_value=fake_result)
        helper_for_mock.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
