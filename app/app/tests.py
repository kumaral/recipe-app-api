"""
Sample test
"""

from django.test import SimpleTestCase


from app import calc


class CalcTest(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """Test subtracting numbers together"""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)
