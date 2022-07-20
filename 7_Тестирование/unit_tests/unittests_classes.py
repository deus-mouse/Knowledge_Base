# -*- coding: utf-8 -*-
import unittest

from helper_for_unittests import Child, House, Wife


class ChildTest(unittest.TestCase):

    def setUp(self):
        self.sweet_home = House()
        self.dasha = Child(name='Даша', house=self.sweet_home)

    def test_sleep(self):
        self.dasha.fullness = 30
        self.dasha.happiness = 100
        self.dasha.sleep()
        self.assertEqual(self.dasha.fullness, 20)
        self.assertEqual(self.dasha.happiness, 100)

    def test_act_full_up(self):
        self.dasha.fullness = 30
        self.dasha.happiness = 100
        self.dasha.act()
        self.assertEqual(self.dasha.fullness, 20)
        self.assertEqual(self.dasha.happiness, 100)

    def test_act_hungry(self):
        self.dasha.fullness = 10
        self.dasha.act()
        self.assertEqual(self.dasha.fullness, 20)


class WifeTest(unittest.TestCase):

    def setUp(self):
        self.sweet_home = House()
        self.anna = Wife(name='Анна Петровна', house=self.sweet_home)

    def test_act_with_shopping(self):
        self.sweet_home.food = 0
        self.anna.fullness = 30
        self.anna.act()
        self.assertEqual(self.anna.fullness, 20)
        self.assertEqual(self.sweet_home.food, 100)

    def test_act_with_buy_fur_coat(self):
        self.sweet_home.food = 100
        self.sweet_home.dirt = 0
        self.sweet_home.money = 1000
        self.anna.happiness = 10
        self.anna.act()
        self.assertEqual(self.anna.fullness, 20)
        self.assertEqual(self.anna.happiness, 70)
        self.assertEqual(self.sweet_home.money, 650)


if __name__ == '__main__':
    unittest.main()


