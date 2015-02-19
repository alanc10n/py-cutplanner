class Planner(object):

    def __init__(self, sizes, needed):
        self.stock = []
        self.stock_sizes = sorted(sizes)
        self.pieces_needed = needed

    def getLargestStock(self):
        return self.stock_sizes[-1]



