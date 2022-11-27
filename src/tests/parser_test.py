import unittest
from parser import parser

class TestParser(unittest.TestCase):
    
    def test_parsing_works(self):
        res = parser.parse("Hello [1]", [1], ["world"])
        self.assertEqual(res, "Hello world")

    def test_multiple_variables_works(self):
        res = parser.parse("Hello [1], hello [2]", [1,2],["foo", "bar"])
        self.assertEqual(res, "Hello foo, hello bar")
    
    def test_multiple_instances_of_one_variable_works(self):
        res = parser.parse("Hello [1][1], bye [1]", [1], ["foo"])
        self.assertEqual(res, "Hello foofoo, bye foo")

    def test_parsing_works_with_numbers(self):
        res = parser.parse("Hello [1]", [1], [1337])
        self.assertEqual(res, "Hello 1337")