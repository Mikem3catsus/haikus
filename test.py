#!/usr/bin/python3

import unittest

def fizzbuzz(number):
    fizzbuzz_dict = {3: "Fizz", 5: "Buzz"}
    return substitutor(number, fizzbuzz_dict)

def substitutor(number, dict):
    return_value = number
    for key in sorted(dict.keys()):
        if number % key == 0:
            return_value = type_aware_append(return_value, dict[key])
    return return_value

def type_aware_append(original, append_value):
    if type(original) == type(""):
        return original + append_value
    return append_value

class TestFizzBuzz(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(fizzbuzz(1),1)
        self.assertEqual(fizzbuzz(2),2)
        self.assertEqual(fizzbuzz(4),4)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()