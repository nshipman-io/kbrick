from kbrick import __version__
from kbrick.kbrick import hello

import unittest


def test_version():
    assert __version__ == '0.1.0'


class TestCLI(unittest.TestCase):
    def test_hello(self):
        tc1 = hello("TestUser")
        tc2 = hello("")
        self.assertEqual(tc1, "Hello, TestUser!")
        self.assertEqual(tc2, "Hello World!")
