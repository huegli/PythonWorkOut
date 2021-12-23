import unittest
from pig_latin import pig_latin
from stringsort import strsort


class Test_Chap02(unittest.TestCase):

    def test_pig_latin(self):
        self.assertEqual('airway', pig_latin('air'))
        self.assertEqual('eatway', pig_latin('eat'))
        self.assertEqual('ythonpay', pig_latin('python'))
        self.assertEqual('omputercay', pig_latin('computer'))
        self.assertEqual('ellohay', pig_latin('hello'))

    def test_strsort1(self):
        self.assertEqual('abc', strsort('cba'))
        self.assertEqual('abcghiopq', strsort('pohigbqac'))
        self.assertEqual('abcefj', strsort('cbjeaf'))
