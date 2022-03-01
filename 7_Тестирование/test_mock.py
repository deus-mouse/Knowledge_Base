import requests
import unittest
import mock

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


class ExternalResourceGetterTest(unittest.TestCase):

    def test_normal(self):
        getter = mock.ExternalResourceGetter(url='bla-bla-bla')
        # fake_result = Mock()
        # fake_result.text = _test_data
        # fake_get_result = Mock(return_value=fake_result)
        requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
