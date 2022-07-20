import unittest
import helper_for_mock


# 1
class ExternalResourceGetterTest1(unittest.TestCase):

    def test_normal(self):
        getter = helper_for_mock.ExternalResourceGetter(url='https://www.python.org/')
        result = getter.run()
        self.assertEqual(result, 454)  # for https://www.python.org/


_test_data = """
1234567
12345
123456789
12
"""


class FakeResult:

    def __init__(self):
        self.text = _test_data


def fake_get_result(*args, **kwargs):
    return FakeResult()

# 2
class ExternalResourceGetterTest2(unittest.TestCase):

    def test_normal(self):
        getter = helper_for_mock.ExternalResourceGetter(url='bla-bla-bla')  # уже не важно какой url
        helper_for_mock.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
