import cutplanner
import unittest

class TestStock(unittest.TestCase):

    def setUp(self):
        self.stock = cutplanner.Stock(120)

    def test_cut(self):
        self.stock.assign_cut(20)
        self.assertEqual(self.stock.remaining_length, 100)


if __name__ == '__main__':
    unittest.main()
