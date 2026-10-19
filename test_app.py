import unittest
from app import add


class TestApp(unittest.TestCase):

    def test_add_positive_values(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
