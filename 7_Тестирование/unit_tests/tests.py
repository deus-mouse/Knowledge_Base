'''
https://www.youtube.com/watch?v=ptssYZR4kus
'''

import unittest
import os
import sys

from main import *


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_float(self) -> float:
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_int(self) -> int:
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self) -> 0:
        self.assertEqual(nitro_salt('sdsd'), 0)


if __name__ == '__main__':
    unittest.main()
