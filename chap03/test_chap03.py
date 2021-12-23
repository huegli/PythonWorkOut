import unittest
from firstlast import firstlast
from mysum import mysum
from alphabetize import alphabetize_names
from repeating import most_repeating_word
from formatsort import format_sort_records

PEOPLE = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Nikolai", "last": "Schlegel", "email": "nikolai.schlegel@gmail.com"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
]

SORTED_PPL = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
    {"first": "Nikolai", "last": "Schlegel", "email": "nikolai.schlegel@gmail.com"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
]

WORDS = ["this", "is", "an", "elementary", "test", "example"]

SUMMIT_PEOPLE = [('Donald', 'Trump', 7.85),
                 ('Vladimir', 'Putin', 3.626),
                 ('Jinping', 'Xi', 10.603)]

SUMMIT_TABLE = """Putin      Vladimir    3.63
Trump      Donald      7.85
Xi         Jinping    10.60
"""


class Test_Chap03(unittest.TestCase):
    def test_firstlast(self):
        self.assertEqual("ac", firstlast("abc"))
        self.assertEqual([1, 4], firstlast([1, 2, 3, 4]))

    def test_mysum(self):
        self.assertEqual("abcdef", mysum("abc", "def"))
        self.assertEqual([1, 2, 3, 4, 5, 6], mysum([1, 2, 3], [4, 5, 6]))
        self.assertEqual(6, mysum(1, 2, 3))

    def test_alphabetize(self):
        self.assertEqual(SORTED_PPL, alphabetize_names(PEOPLE))

    def test_repeating(self):
        self.assertEqual("elementary", most_repeating_word(WORDS))

    def test_formatsort(self):
        self.assertEqual(SUMMIT_TABLE, format_sort_records(SUMMIT_PEOPLE))


if __name__ == "__main__":
    unittest.main()
