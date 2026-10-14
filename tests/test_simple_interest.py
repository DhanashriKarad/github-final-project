import unittest

from simple_interest import simple_interest, total_amount


class SimpleInterestTests(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100.0)
        self.assertEqual(simple_interest(2000, 10, 3), 600.0)

    def test_total_amount(self):
        self.assertEqual(total_amount(1000, 5, 2), 1100.0)
        self.assertEqual(total_amount(2000, 10, 3), 2600.0)


if __name__ == "__main__":
    unittest.main()
