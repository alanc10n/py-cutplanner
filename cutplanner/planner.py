import collections

# simple structure to keep track of a specific piece
Piece = collections.namedtuple('Piece', 'id, length')

class Planner(object):

    def __init__(self, sizes, needed, loss=0.25):
        self.stock = []
        self.stock_sizes = sorted(sizes)
        self.pieces_needed = needed
        self.cut_loss = loss
        self.cur_stock = None

    def get_largest_stock(self):
        return self.stock_sizes[-1]

    def cut_piece(self, piece):
        """ Record the cut for the given piece """
        cur_stock.cut(piece, self.cut_loss)
