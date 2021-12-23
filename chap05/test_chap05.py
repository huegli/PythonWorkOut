import unittest
from io import StringIO

from finalline import get_final_line
from passwd_to_dict import passwd_to_dict
from wordcount import wordcount
from longest_word import find_longest_word, find_all_longest_word
from passwd_to_csv import passwd_to_csv
from scores import print_scores
from reverse import reverse

PASSWD_FILE = StringIO(
    """
# A comment
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
# I am a comment line
_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
"""
)

PASSWD_DICT = {"nobody": -2, "root": 0, "daemon": 1, "_ftp": 98}

PASSWD_CSV_EXPECTED = StringIO(
    """nobody,-2
root,0
daemon,1
_ftp,98
"""
)

WC_FILE = StringIO(
    """
This is a test file.
It contains 28 words and 20 different words.
It also contains 165 characters.
It also contains 11 lines.
It is also self-referential.
Wow!
"""
)

LW_DICT = {
    "1342-0.txt": "http://www.gutenberg.org/1/3/4/1342/",
    "2701-0.txt": "http://www.gutenberg.org/2/7/0/2701/",
    "61105-0.txt": "http://www.gutenberg.org/6/1/1/0/61105/",
    "84-0.txt": "http://www.gutenberg.org/8/84/",
    "pg25525.txt": "http://www.gutenberg.org/2/5/5/2/25525/",
    "pg28860.txt": "http://www.gutenberg.org/2/8/8/6/28860/",
    "pg514.txt": "_________________________________________________",
}

SCORES_RESULT = """
./scores/9b.json
    science: min 35, max 95, average 76.0
    literature: min 38, max 98, average 75.6
    math: min 38, max 100, average 74.6
./scores/9a.json
    science: min 75, max 97, average 86.4
    literature: min 78, max 98, average 83.6
    math: min 65, max 100, average 85.0
"""

IN_FILE = StringIO("""
abc def
ghi jkl
""")


class Test_Chap05(unittest.TestCase):
    def test_get_final_line(self):
        self.assertEqual("    unittest.main()\n", get_final_line("test_chap05.py"))
        self.assertEqual(
            '    print(get_final_line("/etc/passwd"))\n', get_final_line("finalline.py")
        )

    def test_passwd_to_dict(self):
        PASSWD_FILE.seek(0)
        self.assertEqual(PASSWD_DICT, passwd_to_dict(PASSWD_FILE))

    def test_wordcount(self):
        self.assertEqual((161, 28, 7, 20), wordcount(WC_FILE))

    def test_longest_word(self):
        self.assertEqual(
            "http://www.gutenberg.org/1/3/4/1342/",
            find_longest_word("files/1342-0.txt"),
        )
        self.assertEqual(LW_DICT, find_all_longest_word("./files"))

    def test_passwd_to_csv(self):
        PASSWD_FILE.seek(0)
        passwd_csv_actual = StringIO()
        passwd_to_csv(PASSWD_FILE, passwd_csv_actual)
        self.assertEqual(PASSWD_CSV_EXPECTED.getvalue(), passwd_csv_actual.getvalue())

    def test_print_scores(self):
        self.assertEqual(SCORES_RESULT, print_scores("./scores").getvalue())

    def test_reverse(self):
        OUT_FILE = StringIO()
        reverse(IN_FILE, OUT_FILE)
        self.assertEqual(OUT_FILE.getvalue(), CHECK_FILE.getvalue())


if __name__ == "__main__":
    unittest.main()
