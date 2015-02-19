import cutplanner
import unittest

class TestPlanner(unittest.TestCase):

    def setUp(self):
        sizes = [80, 120]
        needed = [10, 25, 75]
        loss = 0.25
        self.planner = cutplanner.Planner(sizes, needed, loss)

    def test_get_largest(self):
        largest = self.planner.get_largest_stock()
        self.assertEqual(largest, 120)

if __name__ == '__main__':
    unittest.main()
