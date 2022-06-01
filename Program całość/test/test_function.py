#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from main import *



class MakeResultTestCase(unittest.TestCase):
    def test_make_result(self):
        result = make_result(1, 5, 3)
        self.assertEqual(result, 50)
    def test_choose_level(self):
        dostepne_poziomy = {1: "Łatwy poziom trudności", 2: "Średni poziom trudnośći", 3: "Wysoki poziom trudności"}
        result = choose_level(dostepne_poziomy)
        self.assertEqual(result, 1)
    def test_choose_category(self):
        dostepne_kategorie = {1: "Zwierzeta", 2: "Rzeczy", 3: "Owoce i Warzywa", 4: "Panstwa"}
        result = choose_category(dostepne_kategorie)
        self.assertEqual(result, 1)
  



if __name__ == '__main__':
    unittest.main()
