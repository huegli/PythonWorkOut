import unittest
from restaurant import restaurant
from rainfall import get_rainfall
from dictdiff import dictdiff
from different import how_many_different_numbers


class Test_Chap04(unittest.TestCase):
    def test_restaurant(self):
        self.assertEqual("Running total is 10", restaurant("sandwich"))
        self.assertEqual("Running total is 17", restaurant("tea"))
        self.assertEqual("Not available", restaurant("elephant"))
        self.assertEqual("Running total is 22", restaurant("icecream"))
        self.assertEqual("Grand total is 22", restaurant(""))

    def test_rainfall(self):
        self.assertEqual({"Boston": 5}, get_rainfall("Boston", 5))
        self.assertEqual({"Boston": 5, "New York": 7}, get_rainfall("New York", 7))
        self.assertEqual({"Boston": 10, "New York": 7}, get_rainfall("Boston", 5))
        self.assertEqual(
            {"Boston": 10, "New York": 7, "Los Angeles": 3},
            get_rainfall("Los Angeles", 3),
        )

    def test_dictdiff(self):
        d1 = {"a": 1, "b": 2, "c": 3}
        d2 = {"a": 1, "b": 2, "c": 4}
        d3 = {"a": 1, "b": 2, "d": 3}
        d4 = {"a": 1, "b": 2, "c": 4}
        d5 = {"a": 1, "b": 2, "d": 4}

        self.assertEqual({}, dictdiff(d1, d1))
        self.assertEqual({"c": [3, 4]}, dictdiff(d1, d2))
        self.assertEqual({"c": [None, 4], "d": [3, None]}, dictdiff(d3, d4))
        self.assertEqual({"c": [3, None], "d": [None, 4]}, dictdiff(d1, d5))

    def test_different(self):
        list1 = [1, 2, 3, 1, 2, 3, 4, 1]
        list2 = [1, 2, 3, 4, 5, 6, 4, 3, 4]
        list3 = [7, 7, 7, 7, 7, 3, 3]

        self.assertEqual(4, how_many_different_numbers(list1))
        self.assertEqual(6, how_many_different_numbers(list2))
        self.assertEqual(2, how_many_different_numbers(list3))


if __name__ == "__main__":
    unittest.main()
