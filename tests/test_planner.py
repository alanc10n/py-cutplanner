import cutplanner
import unittest

class TestPlanner(unittest.TestCase):

    def setUp(self):
        sizes = [50, 80, 120]
        needed = [10, 25, 75]
        loss = 0.25
        self.planner = cutplanner.Planner(sizes, needed, loss)

    def test_largest_stock(self):
        largest = self.planner.largest_stock
        self.assertEqual(largest, 120)

    def test_finalize(self):
        self.planner.cur_stock = cutplanner.Stock(self.planner.largest_stock)
        self.planner.cut_piece(cutplanner.Piece(1, 60))
        self.planner.finalize_stock()
        self.assertEqual(len(self.planner.stock), 1)
        self.assertEqual(self.planner.stock[0].length, 80)

if __name__ == '__main__':
    unittest.main()
