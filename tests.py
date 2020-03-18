#!/usr/bin/python3
from fibonacci_prime_numbers import fib, is_prime_number, prime_fibonacci_numbers
import unittest

class FibonacciPrimeNumbers(unittest.TestCase):
    """Tests for 'fib', 'is_prime_number' and 'prime_fibonacci_numbers' function."""

    def test_fib_nth_element_is_correct(self):
        """Check if 1st, 2nd, 5th and 10th element of fibonacci sequence is correct"""
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(9), 34)

    def test_fib_negative_input_returns_message(self):
        """Check if negative input returns correct message"""
        self.assertEqual(fib(-1), "Input must be not negative integer")

    def test_fib_non_integer_input_returns_message(self):
        """Check if string type input returns correct message"""
        self.assertEqual(fib("test"), "Input must be not negative integer")

    def test_is_five_prime_number(self):
        """Check if five is correctly determined to be prime"""
        self.assertTrue(is_prime_number(5))

    def test_is_four_non_prime_number(self):
        """Check if four is correctly determined not to be prime"""
        self.assertFalse(is_prime_number(4))

    def test_is_zero_not_prime_number(self):
        """Check if zero is correctly determined not to be prime"""
        self.assertFalse(is_prime_number(0))

    def test_is_negative_input_not_prime_number(self):
        """Check if negative number is correctly determined not to be prime"""
        self.assertFalse(is_prime_number(-1))

    def test_is_non_integer_input_not_prime_number(self):
        """Check if not integer number is correctly determined not to be prime"""
        self.assertFalse(is_prime_number(-1))

    def test_prime_fibonacci_numbers_return_correct_list_of_n_primes(self):
        """Check if 'prime_fibonacci_numbers' returns correct list of n prime values from fibonacci sequence"""
        self.assertEqual(prime_fibonacci_numbers(1), [2])
        self.assertEqual(prime_fibonacci_numbers(3), [2, 3, 5])
        self.assertEqual(prime_fibonacci_numbers(5), [2, 3, 5, 13, 89])

    def test_prime_fibonacci_numbers_returns_empty_list_for_zero_input(self):
        """Check if 'prime_fibonacci_numbers' returns correctly empty list for input equal to 0"""
        self.assertEqual(prime_fibonacci_numbers(0), [])

    def test_prime_fibonacci_numbers_returns_message_for_negative_input(self):
        """Check if 'prime_fibonacci_numbers' returns correctly message for negative input"""
        self.assertEqual(prime_fibonacci_numbers(-1), "Input must be not negative integer")
        self.assertEqual(prime_fibonacci_numbers(-6), "Input must be not negative integer")

    def test_prime_fibonacci_numbers_returns_message_for_non_integer_input(self):
        """Check if 'prime_fibonacci_numbers' returns correctly message for negative input"""
        self.assertEqual(prime_fibonacci_numbers(0.5), "Input must be not negative integer")
        self.assertEqual(prime_fibonacci_numbers("4"), "Input must be not negative integer")

if __name__ == '__main__':
    unittest.main()