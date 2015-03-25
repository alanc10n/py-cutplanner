import cutplanner
import unittest

class TestPlanner(unittest.TestCase):

    def setUp(self):
        sizes = [50, 80, 120]
        needed = [10, 25, 75]
        loss = 0.25
        self.planner = cutplanner.Planner(sizes, needed, loss)

    def test_init_pieces(self):
        self.assertEqual(len(self.planner.pieces_needed), 3)
        self.assertEqual(self.planner.pieces_needed[0].length, 75)

    def test_init_stock(self):
        self.assertEqual(len(self.planner.stock_sizes), 3)
        self.assertEqual(self.planner.stock_sizes, [50, 80, 120])

    def test_largest_stock(self):
        largest = self.planner.largest_stock
        self.assertEqual(largest, 120)

    def test_finalize(self):
        self.planner.cur_stock = cutplanner.Stock(self.planner.largest_stock)
        self.planner.cut_piece(cutplanner.Piece(1, 60))
        self.planner.finalize_stock()
        self.assertEqual(len(self.planner.stock), 1)
        self.assertEqual(self.planner.stock[0].length, 80)

    def test_make_cuts(self):
        self.planner.make_cuts()
        self.assertTrue(len(self.planner.pieces_needed) == 0)
        self.assertTrue(len(self.planner.stock) == 1)
        self.assertEqual(self.planner.stock[0].used_length, 110.75)

if __name__ == '__main__':
    unittest.main()
