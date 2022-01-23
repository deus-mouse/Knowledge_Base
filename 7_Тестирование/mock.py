import requests
import unittest
from unittest.mock import Mock


class ExternalResourceGetter:

    def __init__(self, url):
        self.url = url
        self.data = None

    def run(self):
        self.data = self.get_data()
        result = self.proceed_data()
        return result

    def get_data(self):
        response = requests.get(self.url)
        return response.text

    def proceed_data(self):
        # max_length = 0
        # for line in self.data.split('\n'):
        #     if len(line) > max_length:
        #         max_length = len(line)
        max_length = max([len(line) for line in self.data.split('\n')])
        return max_length


if __name__ == '__main__':
    getter = ExternalResourceGetter(url='https://www.jetbrains.com/pycharm/')

    data = getter.run()
    print(data)



_test_data = """
1234567
12345
123456789
12
"""

# class FakeResult:
#
#     def __init__(self):
#         self.text = _test_data


# def fake_get_result(*args, **kwargs):
#     return FakeResult()


class ExternalResourceGetterTest(unittest.TestCase):

    def test_normal(self):
        getter = ExternalResourceGetter(url='bla-bla-bla')
        fake_result = Mock()
        fake_result.text = _test_data
        fake_get_result = Mock(return_value=fake_result)
        requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
