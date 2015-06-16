import collections
from .stock import Stock

# simple structure to keep track of a specific piece
Piece = collections.namedtuple('Piece', 'id, length')


class Planner(object):

    def __init__(self, sizes, needed, loss=0.25):
        self.stock = []
        self.stock_sizes = sorted(sizes)
        self.pieces_needed = [Piece(i, s) for i, s in enumerate(needed)]
        self.pieces_needed.reverse()
        self.cut_loss = loss
        self.cur_stock = None

        # set the algorithm to use, hard code for now
        self.apply_algo = self.apply_next_fit

    @property
    def largest_stock(self):
        return self.stock_sizes[-1]

    def cut_piece(self, piece):
        """ Record the cut for the given piece """
        self.cur_stock.cut(piece, self.cut_loss)

    def finalize_stock(self):
        """ Takes current stock out of use, attempts to shrink """
        # shrink as much as possible
        for smaller in self.stock_sizes[-2::-1]:
            if self.cur_stock.shrink(smaller) is None:
                break

        self.stock.append(self.cur_stock)

    def apply_next_fit(self, piece):
        """ Cut from current stock until unable, then move to new stock """
        if self.cur_stock.remaining_length < piece.length + self.cut_loss:
            # finalize current stock and get fresh stock
            self.finalize_stock()
            self.cur_stock = Stock(self.largest_stock)

        self.cur_stock.cut(piece, self.cut_loss)

    def make_cuts(self):
        self.cur_stock = Stock(self.largest_stock)

        while self.pieces_needed:
            piece = self.pieces_needed.pop()
            self.apply_algo(piece)

        self.finalize_stock()
