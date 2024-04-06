import unittest
import datetime
import sys
from mymy.main import hello_world, _DATE_FMT


class MyFirstTest(unittest.TestCase):
    def test_func(self):
        msg, pymsg = hello_world()
        py = sys.version.split()[0]
        now = datetime.datetime.now().strftime(_DATE_FMT) 
        self.assertEqual(now, msg)
        self.assertEqual(py, pymsg)

