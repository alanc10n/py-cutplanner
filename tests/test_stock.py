import cutplanner
import unittest

class TestStock(unittest.TestCase):

    def setUp(self):
        self.stock = cutplanner.Stock(120)
        self.piece = cutplanner.Piece(1, 20)

    def test_cut(self):
        self.stock.cut(self.piece)
        self.assertEqual(self.stock.remaining_length, 100)

    def test_used_length(self):
        self.assertEqual(self.stock.used_length, 0)
        self.stock.cut(self.piece)
        self.assertEqual(self.stock.used_length, self.piece.length)

    def test_shrink(self):
        self.stock.cut(self.piece)
        print "{0} remaining, {1} used".format(self.stock.remaining_length, self.stock.used_length)

        new_len = self.stock.shrink(80)
        self.assertEqual(new_len, 80)

if __name__ == '__main__':
    unittest.main()
