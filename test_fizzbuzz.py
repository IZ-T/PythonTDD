import unittest

from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def test_check_For1Returns1(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(1)
        self.assertEqual("1", result)

    def test_check_For2Returns2(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(2)
        self.assertEqual("2", result)

    def test_check_For3ReturnsFizz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(3)
        self.assertEqual("Fizz", result)

    def test_check_For3ReturnsFizz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(6)
        self.assertEqual("Fizz", result)

    def test_check_For5ReturnsBuzz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(5)
        self.assertEqual("Buzz", result)

    def test_check_For10ReturnsBuzz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(10)
        self.assertEqual("Buzz", result)

    def test_check_For15ReturnsFizzBuzz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(15)
        self.assertEqual("FizzBuzz", result)

    def test_check_For45ReturnsBuzz(self):
        fizz_buzz = FizzBuzz()
        result = fizz_buzz.check(45)
        self.assertEqual("FizzBuzz", result)
